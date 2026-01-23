import threading
from typing import Any, Dict

# In-memory idempotency store (Phase 7B only)
# Key: idempotency_key
# Value: response payload
_idempotency_store: Dict[str, Any] = {}
_lock = threading.Lock()

def get_cached(key: str):
    with _lock:
        return _idempotency_store.get(key)

def set_cached(key: str, value: Any):
    with _lock:
        _idempotency_store[key] = value
