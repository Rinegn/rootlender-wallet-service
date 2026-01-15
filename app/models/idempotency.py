from sqlalchemy import Column, Integer, String, DateTime, UniqueConstraint, func

from app.db.base import Base


class IdempotencyKey(Base):
    __tablename__ = "idempotency_keys"

    id = Column(Integer, primary_key=True)
    key = Column(String(64), nullable=False)
    wallet_id = Column(Integer, nullable=False)
    operation = Column(String(32), nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    __table_args__ = (
        UniqueConstraint("key", "wallet_id", "operation", name="uq_idempotency"),
    )
