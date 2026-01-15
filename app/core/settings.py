from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_name: str = "rootlender-wallet-service"
    service_name: str = "rootlender-wallet-service"
    environment: str = "local"
    port: int = 8010

    # Dependencies (soft)
    config_service_url: str | None = None
    service_registry_url: str | None = None

    model_config = SettingsConfigDict(
        env_file=".env",
        env_prefix="",
        extra="ignore",
        case_sensitive=False,
    )


settings = Settings()
