from datetime import datetime, timedelta
from typing import Optional


def utcnow() -> datetime:
    """Centralized UTC time helper."""
    return datetime.utcnow()


def minutes_from_now(minutes: int) -> datetime:
    return utcnow() + timedelta(minutes=minutes)
