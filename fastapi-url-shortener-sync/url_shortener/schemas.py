from pydantic import BaseModel

class URLRequest(BaseModel):
    target_url: str

class ShortURLResponse(BaseModel):
    short_url: str
    secret_key: str


class URL(BaseModel):
    target_url: str
    short_url_key: str
    clicks: int
    is_active: bool
    secret_key: str

    class Config:
        orm_mode: bool = True

