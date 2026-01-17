from fastapi import FastAPI
from app.core.settings import settings
from app.clients.ledger_client import fetch_balance


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
    return {
        "service": settings.service_name,
        "environment": settings.environment,
        "status": "ok",
    }


@app.get("/wallets/{user_id}/balance")
def wallet_balance(user_id: str):
    """
    Wallet owns orchestration, Ledger owns truth.
    Wallet does ZERO balance math.
    """
    bal = fetch_balance(user_id)
    if not bal:
        # Safe failure: service stays up, caller sees dependency unavailable
        return {
            "user_id": user_id,
            "currency": "USD",
            "balance": None,
            "source": "ledger",
            "status": "unavailable",
        }

    # Pass-through (Ledger-owned)
    bal["source"] = "ledger"
    bal["status"] = "ok"
    return bal
