from functools import lru_cache

from pydantic import BaseSettings


class Settings(BaseSettings):
    database_url: str

    # Can this find the .env file?
    class Config:
        env_file = ".env"


@lru_cache()
def get_settings():
    return Settings()
