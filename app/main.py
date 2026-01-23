from fastapi import FastAPI

from app.middleware.correlation import correlation_middleware
from app.storage.bootstrap import ensure_tables
from app.clients.service_registry_client import register_service

from app.routers.health import router as health_router
from app.routers.balances import router as balances_router
from app.routers.transactions import router as transactions_router

app = FastAPI(title="RootLender Wallet Service")

# Correlation middleware
app.middleware("http")(correlation_middleware)

# Routers
app.include_router(health_router)
app.include_router(balances_router)
app.include_router(transactions_router)

@app.on_event("startup")
def startup():
    # Ensure wallet-local tables exist
    ensure_tables()

    # Register service with registry
    register_service(port=8010)
