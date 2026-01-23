import requests
from app.core.service import SERVICE_NAME

REGISTRY_URL = "http://127.0.0.1:8002"
ENVIRONMENT = "local"

def register_service(port: int):
    payload = {
        "service_name": SERVICE_NAME,
        "base_url": f"http://127.0.0.1:{port}",
        "environment": ENVIRONMENT,
    }

    try:
        resp = requests.post(
            f"{REGISTRY_URL}/register",
            json=payload,
            timeout=5,
        )
        resp.raise_for_status()
        print(f"[registry] registered {SERVICE_NAME}")
    except Exception as e:
        # Phase 7A must NEVER block startup
        print(f"[registry] registration skipped: {e}")

def discover(service_name: str):
    resp = requests.get(f"{REGISTRY_URL}/services", timeout=5)
    resp.raise_for_status()

    for svc in resp.json():
        if svc["service_name"] == service_name:
            return svc

    raise RuntimeError(f"Service not found: {service_name}")
