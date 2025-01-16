from pydantic_settings import BaseSettings
from functools import lru_cache

class Settings(BaseSettings):
    env_name: str = "local"
    base_url: str = "http://localhost:8080"
    db_uri: str = "sqlite:///./url_shortener.db"

    class Config:
        env_file = ".env"

@lru_cache
def get_settings() -> Settings:
    settings = Settings()
    print(f"Loading settings for environment: {settings.env_name}")
    return settings



