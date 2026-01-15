from decimal import Decimal
from typing import Optional

from sqlalchemy.orm import Session

from app.models.wallet import Wallet


class WalletService:
    """
    Business logic for wallet operations.
    No FastAPI or HTTP concerns should exist here.
    """

    @staticmethod
    def get_wallet_by_id(db: Session, wallet_id: int) -> Optional[Wallet]:
        return (
            db.query(Wallet)
            .filter(Wallet.id == wallet_id)
            .first()
        )

    @staticmethod
    def get_wallet_by_user_id(
        db: Session,
        user_id: int,
        currency: str = "USD",
    ) -> Optional[Wallet]:
        return (
            db.query(Wallet)
            .filter(
                Wallet.user_id == user_id,
                Wallet.currency == currency,
            )
            .first()
        )

    @staticmethod
    def create_wallet(
        db: Session,
        user_id: int,
        currency: str = "USD",
    ) -> Wallet:
        wallet = Wallet(
            user_id=user_id,
            currency=currency,
            balance=Decimal("0.00"),
            status="active",
        )

        db.add(wallet)
        db.commit()
        db.refresh(wallet)

        return wallet
