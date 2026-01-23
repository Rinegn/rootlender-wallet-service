import uuid
from fastapi import APIRouter, HTTPException, Request
from pydantic import BaseModel

from app.services.transaction_orchestrator import purchase
from app.storage.wallet_transactions import tx_get

router = APIRouter(prefix="/wallet/transactions", tags=["wallet-transactions"])

class PurchaseRequest(BaseModel):
    user_id: str
    amount: float
    currency: str
    reference_id: str

@router.post("/purchase")
def purchase_route(body: PurchaseRequest, request: Request):
    correlation_id = getattr(request.state, "correlation_id", None)

    base_idem_key = request.headers.get("Idempotency-Key")
    if not base_idem_key:
        base_idem_key = f"wallet-purchase-{body.user_id}-{uuid.uuid4()}"

    try:
        return purchase(
            user_id=body.user_id,
            amount=body.amount,
            currency=body.currency,
            reference_id=body.reference_id,
            correlation_id=correlation_id,
            base_idem_key=base_idem_key,
        )
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/{tx_id}")
def tx_status(tx_id: str):
    row = tx_get(tx_id)
    if not row:
        raise HTTPException(status_code=404, detail="Not Found")
    return dict(row)
