from fastapi import FastAPI

from app.middleware.correlation import correlation_middleware
from app.routers.health import router as health_router
from app.routers.holds import router as holds_router
from app.routers.transactions import router as transactions_router

app = FastAPI()

# Middleware
app.middleware("http")(correlation_middleware)

# Routers
app.include_router(health_router)
app.include_router(holds_router)
app.include_router(transactions_router)
