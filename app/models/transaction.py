from sqlalchemy import (
    Column,
    Integer,
    Numeric,
    String,
    DateTime,
    ForeignKey,
    func,
)

from app.db.base import Base


class Transaction(Base):
    __tablename__ = "transactions"

    id = Column(Integer, primary_key=True, index=True)

    wallet_id = Column(Integer, ForeignKey("wallets.id"), nullable=False)

    amount = Column(Numeric(precision=12, scale=2), nullable=False)
    balance_after = Column(Numeric(precision=12, scale=2), nullable=False)

    currency = Column(String(3), nullable=False)
    description = Column(String(255), nullable=True)

    created_at = Column(DateTime(timezone=True), server_default=func.now())
