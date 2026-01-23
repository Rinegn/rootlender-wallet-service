from pydantic_settings import BaseSettings
from pydantic import Field

class Settings(BaseSettings):
    database_url: str = Field(
        default="sqlite:///./wallet.db",
        env="DATABASE_URL",
        description="Wallet local database"
    )

    class Config:
        extra = "forbid"

def get_settings() -> Settings:
    return Settings()
