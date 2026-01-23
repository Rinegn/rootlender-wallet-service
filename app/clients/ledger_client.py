import requests
from app.clients.service_registry_client import discover

LEDGER_SERVICE = "ledger-service"

def _base():
    svc = discover(LEDGER_SERVICE)
    return svc["base_url"].rstrip("/")

def get_balance(user_id: str):
    r = requests.get(f"{_base()}/balances/{user_id}", timeout=5)
    r.raise_for_status()
    return r.json()

def create_hold(payload: dict):
    r = requests.post(f"{_base()}/holds", json=payload, timeout=5)
    r.raise_for_status()
    return r.json()

def capture_hold(hold_id: str):
    r = requests.post(f"{_base()}/holds/{hold_id}/capture", timeout=5)
    r.raise_for_status()
    return r.json()

def release_hold(hold_id: str):
    r = requests.post(f"{_base()}/holds/{hold_id}/release", timeout=5)
    r.raise_for_status()
    return r.json()

def create_entry(payload: dict):
    r = requests.post(f"{_base()}/entries", json=payload, timeout=5)
    r.raise_for_status()
    return r.json()
