from fastapi import FastAPI
from app.core.settings import settings
from app.clients.config_client import fetch_wallet_config

app = FastAPI(
    title=settings.app_name,
    version="1.0.0",
)


@app.get("/")
def root():
    return {
        "service": settings.service_name,
        "environment": settings.environment,
        "status": "running",
    }


@app.get("/health")
def health():
    return {"status": "ok"}


@app.get("/_debug/config")
def debug_config():
    return {
        "config": fetch_wallet_config()
    }
