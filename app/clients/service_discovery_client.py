import httpx
from app.core.settings import settings


class ServiceDiscoveryClient:
    def __init__(self):
        self._cache: dict[str, str] = {}

    def get_service_url(self, service_name: str) -> str | None:
        if service_name in self._cache:
            return self._cache[service_name]

        if not settings.service_registry_url:
            return None

        try:
            with httpx.Client(timeout=5.0) as client:
                resp = client.get(f"{settings.service_registry_url}/services")
                resp.raise_for_status()
                services = resp.json()

            service = services.get(service_name)
            if not service:
                return None

            base_url = service.get("base_url")
            if base_url:
                self._cache[service_name] = base_url

            return base_url
        except Exception:
            return None
