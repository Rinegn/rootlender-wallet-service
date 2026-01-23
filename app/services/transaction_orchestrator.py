import uuid
from app.services.idempotency import get_cached, set_cached
from app.domain.transaction_state import TransactionState
from app.clients.ledger_client import (
    create_hold,
    capture_hold,
    create_entry,
)

def purchase(data: dict):
    idem_key = data.get(
        "idempotency_key",
        f"txn-{data['user_id']}-{uuid.uuid4()}",
    )

    cached = get_cached(idem_key)
    if cached:
        return cached

    state = TransactionState.INITIATED

    try:
        hold = create_hold({
            "user_id": data["user_id"],
            "amount": data["amount"],
            "currency": data["currency"],
            "idempotency_key": idem_key,
        })
        state = TransactionState.HOLD_PLACED

        entry = create_entry({
            "user_id": data["user_id"],
            "amount": data["amount"],
            "currency": data["currency"],
            "direction": "debit",
            "reference_type": "purchase",
            "reference_id": hold["hold_id"],
            "idempotency_key": idem_key,
        })
        state = TransactionState.ENTRY_POSTED

        capture_hold({
            "hold_id": hold["hold_id"],
            "idempotency_key": idem_key,
        })

        result = {
            "state": TransactionState.COMPLETED,
            "hold": hold,
            "entry": entry,
        }

        return set_cached(idem_key, result)

    except Exception as e:
        return set_cached(idem_key, {
            "state": TransactionState.FAILED,
            "error": str(e),
        })
