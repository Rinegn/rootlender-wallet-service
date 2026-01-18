from fastapi import APIRouter
from app.clients.ledger_client import create_hold, capture_hold, release_hold

router = APIRouter(prefix="/wallet", tags=["wallet"])


@router.post("/holds")
def request_hold(payload: dict):
    return create_hold(payload)


@router.post("/holds/{hold_id}/capture")
def capture(hold_id: str):
    return capture_hold(hold_id)


@router.post("/holds/{hold_id}/release")
def release(hold_id: str):
    return release_hold(hold_id)
