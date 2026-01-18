from fastapi import APIRouter, HTTPException, Query
from app.clients.ledger_client import get_balance


router = APIRouter(prefix="/wallet/balances", tags=["wallet-balances"])


@router.get("/{user_id}")
def read_wallet_balance(
    user_id: str,
    currency: str = Query("USD", min_length=3, max_length=3),
):
    try:
        return get_balance(user_id=user_id, currency=currency.upper())
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
