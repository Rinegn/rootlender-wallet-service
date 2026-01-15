from functools import lru_cache
from pydantic import BaseSettings, Field


class Settings(BaseSettings):
    # -------------------------
    # Application
    # -------------------------
    app_name: str = Field("rootlender-wallet-service", env="APP_NAME")
    app_env: str = Field("development", env="APP_ENV")
    debug: bool = Field(False, env="DEBUG")

    # -------------------------
    # Server
    # -------------------------
    host: str = Field("0.0.0.0", env="HOST")
    port: int = Field(8000, env="PORT")

    # -------------------------
    # Database
    # -------------------------
    database_url: str = Field(..., env="DATABASE_URL")

    # -------------------------
    # Security
    # -------------------------
    jwt_secret: str = Field(..., env="JWT_SECRET")
    jwt_algorithm: str = Field("HS256", env="JWT_ALGORITHM")
    access_token_expires_minutes: int = Field(60, env="ACCESS_TOKEN_EXPIRE_MINUTES")

    # -------------------------
    # Logging
    # -------------------------
    log_level: str = Field("INFO", env="LOG_LEVEL")

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


@lru_cache
def get_settings() -> Settings:
    return Settings()
