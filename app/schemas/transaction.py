from decimal import Decimal
from typing import Optional

from pydantic import BaseModel, Field


class TransactionBase(BaseModel):
    wallet_id: int = Field(..., example=1)
    amount: Decimal = Field(..., example="25.00")
    currency: str = Field("USD", example="USD")
    description: Optional[str] = Field(None, example="Wallet credit")


class TransactionCreate(TransactionBase):
    pass


class TransactionRead(TransactionBase):
    id: int
    balance_after: Decimal

    class Config:
        orm_mode = True
