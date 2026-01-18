from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field
from app.clients.ledger_client import create_hold, capture_hold


router = APIRouter(prefix="/wallet/holds", tags=["wallet-holds"])


class HoldCreate(BaseModel):
    user_id: str
    amount: float = Field(gt=0)
    currency: str = Field(min_length=3, max_length=3)
    expires_in_seconds: int = Field(gt=0, le=86400)


@router.post("")
def place_hold(data: HoldCreate):
    try:
        payload = data.model_dump()
        payload["currency"] = payload["currency"].upper()
        return create_hold(payload)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.post("/{hold_id}/capture")
def finalize_hold(hold_id: str):
    try:
        return capture_hold(hold_id)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
