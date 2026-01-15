from fastapi import FastAPI

from app.api.v1.routes.health import router as health_router
from app.api.v1.routes.wallet import router as wallet_router
from app.core.config import get_settings
from app.utils.logging import setup_logging

settings = get_settings()

# Initialize logging BEFORE app creation
setup_logging()

app = FastAPI(
    title=settings.app_name,
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc",
    debug=settings.debug,
)

# -----------------------------
# ROUTERS
# -----------------------------
app.include_router(
    health_router,
    prefix="/api/v1",
    tags=["health"],
)

app.include_router(
    wallet_router,
    prefix="/api/v1",
    tags=["wallets"],
)
