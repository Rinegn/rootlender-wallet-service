import httpx
from app.core.settings import settings


def register_self(base_url: str) -> None:
    if not settings.service_registry_url:
        return

    payload = {
        "service_name": settings.service_name,
        "base_url": base_url,
        "environment": settings.environment,
    }

    try:
        with httpx.Client(timeout=5.0) as client:
            client.post(
                f"{settings.service_registry_url}/register",
                json=payload,
            )
    except Exception:
        pass
