# TODO USE ASYNCIO AND SLQALCHEMY[ASYNC]
import secrets
from fastapi import Depends, FastAPI, HTTPException, Request
from fastapi.responses import RedirectResponse
from sqlalchemy.orm import Session
from url_shortener import models, schemas, database
import validators

app = FastAPI()

models.Base.metadata.create_all(bind=database.engine)


@app.get("/")
def read_root():
    return {"Hello": "World"}

# @app.post("/url", response_model=schemas.ShortURLResponse)
@app.post("/url", response_model=schemas.URL)
def create_short_url(url: schemas.URLRequest, db: Session = Depends(database.get_db)) -> schemas.ShortURLResponse:
    if not validators.url(url.target_url):
        # Can become its own function to be reused
        raise HTTPException(status_code=400, detail="Provided URL is not valid")

    # TODO Refactor hard-coded
    chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    # TODO refactor DRY -> extract a method to create random keys (makes it theoertically more testable as well)
    key = "".join(secrets.choice(chars) for _ in range(5))
    secret_key = "".join(secrets.choice(chars) for _ in range(8))

    # TODO refactor dealing with database elsewhere
    # TODO refactor: check for existence of the rand key as well
    # TODO refactor: implement caching on top of DB requests
    db_url = models.URL(
        target_url=url.target_url, short_url_key=key, secret_key=secret_key
    )
    db.add(db_url)
    db.commit()
    db.refresh(db_url)

    return db_url

@app.get("/{url_key}")
def redirect_to_target(
        url_key: str,
        # request: Request,
        db: Session = Depends(database.get_db)
    ) -> RedirectResponse:

    # TODO refactor: dealing with DB elsewhere
    # If some method needs a db session to operate on, it should accept the session as a paramter
    # NOTE the WALRUS operator
    if db_url := (
        db.query(models.URL)
        .filter(models.URL.short_url_key == url_key, models.URL.is_active == True)
        .first()
    ):
        return RedirectResponse(url=str(db_url.target_url))
    else:
        # Can become a method called raise_not_found(request: Request)
        raise HTTPException(status_code=404, detail=f"URL not found: {url_key}")

