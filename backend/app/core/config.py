from pydantic_settings import BaseSettings
from pydantic import AnyHttpUrl
from typing import List


class Settings(BaseSettings):
    DATABASE_URL: str
JWT_SECRET_KEY: str = "change_me"
JWT_ALGORITHM: str = "HS256"
JWT_EXPIRE_MINUTES: int = 60


COOKIE_NAME: str = "access_token"
COOKIE_SECURE: bool = False
COOKIE_SAMESITE: str = "lax" # "lax"|"strict"|"none"


ALLOWED_ORIGINS: str = "http://localhost:3000"


GOOGLE_CLIENT_ID: str = ""
GOOGLE_CLIENT_SECRET: str = ""
GOOGLE_REDIRECT_URI: str = ""


GITHUB_CLIENT_ID: str = ""
GITHUB_CLIENT_SECRET: str = ""
GITHUB_REDIRECT_URI: str = ""


class Config:
    env_file = ".env"


settings = Settings()