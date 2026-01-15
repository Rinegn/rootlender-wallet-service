import httpx
from app.clients.service_registry_client import discover_services


def validate_token_soft(token: str) -> dict | None:
    services = discover_services()
    if not services:
        return None

    iam = services.get("rootlender-iam-service")
    if not iam:
        return None

    try:
        with httpx.Client(timeout=3.0) as client:
            resp = client.get(
                f"{iam['base_url']}/health",
                headers={"Authorization": f"Bearer {token}"},
            )
            if resp.status_code == 200:
                return {
                    "iam_reachable": True,
                    "iam_response": resp.json(),
                }
    except Exception:
        pass

    return None
