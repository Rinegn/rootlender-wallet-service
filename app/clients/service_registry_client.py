import httpx
from app.core.settings import settings


def discover_services() -> dict | None:
    if not settings.service_registry_url:
        return None

    try:
        with httpx.Client(timeout=3.0) as client:
            resp = client.get(f"{settings.service_registry_url}/services")
            if resp.status_code == 200:
                return resp.json()
    except Exception:
        pass

    return None
