from sqlalchemy import Column, Integer, String, Numeric, DateTime, func

from app.db.base import Base


class Wallet(Base):
    __tablename__ = "wallets"

    id = Column(Integer, primary_key=True, index=True)

    # Business identifiers
    user_id = Column(Integer, nullable=False, index=True)
    currency = Column(String(3), nullable=False, default="USD")

    # Financials
    balance = Column(Numeric(precision=12, scale=2), nullable=False, default=0)

    # Metadata
    status = Column(String(20), nullable=False, default="active")

    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now(),
    )
