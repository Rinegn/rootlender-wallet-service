import httpx
from app.core.settings import settings
from app.clients.service_registry_discovery import discover_service_base_url


LEDGER_SERVICE_NAME = "rootlender-ledger-service"


def _ledger_base_url() -> str | None:
    # 1) Direct override wins
    if settings.ledger_service_url:
        return settings.ledger_service_url.rstrip("/")

    # 2) Soft discovery via registry
    discovered = discover_service_base_url(LEDGER_SERVICE_NAME)
    if discovered:
        return discovered.rstrip("/")

    return None


def fetch_balance(user_id: str) -> dict | None:
    """
    Read-only call to Ledger balance endpoint.
    Returns dict on success, None on any failure.
    """
    base = _ledger_base_url()
    if not base:
        return None

    try:
        with httpx.Client(timeout=3.0) as client:
            r = client.get(f"{base}/balances/{user_id}")
            if r.status_code == 200:
                return r.json()
    except Exception:
        return None

    return None
