from fastapi import FastAPI
from app.core.settings import settings
from app.clients.service_registry_client import register_self

app = FastAPI(
    title=settings.app_name,
    version="1.0.0",
)


@app.on_event("startup")
def register_with_service_registry():
    register_self(base_url=f"http://127.0.0.1:{settings.port}")


@app.get("/")
def root():
    return {
        "service": settings.service_name,
        "environment": settings.environment,
        "status": "running",
    }


@app.get("/health")
def health():
    return {
        "service": settings.service_name,
        "environment": settings.environment,
        "status": "ok",
    }
