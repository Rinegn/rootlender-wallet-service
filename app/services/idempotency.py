"""
Wallet-local idempotency store.
Phase 7B: deterministic retries
"""

_cache = {}

def get_cached(key: str):
    return _cache.get(key)

def set_cached(key: str, value):
    _cache[key] = value
    return value
