import httpx
from app.core.settings import settings


def discover_service_base_url(service_name: str) -> str | None:
    """
    Soft discovery:
    - If SERVICE_REGISTRY_URL not set, return None
    - If registry unreachable, return None
    """
    if not settings.service_registry_url:
        return None

    try:
        with httpx.Client(timeout=2.5) as client:
            r = client.get(f"{settings.service_registry_url}/services")
            if r.status_code != 200:
                return None

            data = r.json()  # expected: { "svc": { "base_url": "...", "environment": "local" }, ... }
            svc = data.get(service_name)
            if not svc:
                return None

            base_url = svc.get("base_url")
            if isinstance(base_url, str) and base_url.startswith("http"):
                return base_url
    except Exception:
        return None

    return None
