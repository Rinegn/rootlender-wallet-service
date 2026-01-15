import httpx
from app.clients.service_registry_client import discover_services


def fetch_balance_soft(user_id: str = "debug-user") -> dict | None:
    services = discover_services()
    if not services:
        return None

    ledger = services.get("rootlender-ledger-service")
    if not ledger:
        return None

    try:
        with httpx.Client(timeout=3.0) as client:
            resp = client.get(f"{ledger['base_url']}/health")
            if resp.status_code == 200:
                return {
                    "ledger_reachable": True,
                    "ledger_response": resp.json(),
                    "user_id": user_id,
                    "balance": "0.00 (mock)",
                }
    except Exception:
        pass

    return None
