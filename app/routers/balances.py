from fastapi import APIRouter, Request
from app.clients.ledger_client import get_balance

router = APIRouter(prefix="/wallet/balances", tags=["wallet-balances"])

@router.get("/{user_id}")
def wallet_balance(user_id: str, currency: str, request: Request):
    correlation_id = getattr(request.state, "correlation_id", None)
    return get_balance(user_id=user_id, currency=currency, correlation_id=correlation_id)
