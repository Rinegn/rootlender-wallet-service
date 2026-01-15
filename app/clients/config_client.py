import httpx
from app.core.settings import settings


def fetch_wallet_config() -> dict | None:
    if not settings.config_service_url:
        return None

    try:
        with httpx.Client(timeout=3.0) as client:
            resp = client.get(f"{settings.config_service_url}/health")
            if resp.status_code == 200:
                return resp.json()
    except Exception:
        pass

    return None
