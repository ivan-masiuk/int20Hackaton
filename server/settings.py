"""Settings for FastApi app"""

from pydantic import BaseSettings
from pydantic.fields import Field


class Settings(BaseSettings):
    """App settings"""
    server_host: str = "127.0.0.1"
    server_port: int = 8000

    access_token_expire_minutes: int = Field(..., env="ACCESS_TOKEN_EXPIRE_MINUTES")
    secret_key: str = Field(..., env="SECRET_KEY")
    algorithm: str = Field(..., env="ALGORITHM")


settings = Settings(
    _env_file=".env",
    _env_file_encoding="utf-8",
)
