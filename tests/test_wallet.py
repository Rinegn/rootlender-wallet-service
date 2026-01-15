from decimal import Decimal

from app.schemas.wallet import WalletCreate, WalletRead
from app.models.wallet import Wallet


def test_wallet_schema_creation():
    """
    Basic sanity test to ensure WalletCreate schema
    can be instantiated without errors.
    """
    payload = WalletCreate(
        user_id=1,
        currency="USD",
    )

    assert payload.user_id == 1
    assert payload.currency == "USD"


def test_wallet_model_attributes():
    """
    Ensure Wallet model exposes expected attributes.
    This does NOT touch the database.
    """
    wallet = Wallet(
        user_id=1,
        currency="USD",
        balance=Decimal("0.00"),
        status="active",
    )

    assert wallet.user_id == 1
    assert wallet.currency == "USD"
    assert wallet.balance == Decimal("0.00")
    assert wallet.status == "active"
