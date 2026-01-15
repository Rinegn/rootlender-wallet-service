from decimal import Decimal
from typing import Optional

from pydantic import BaseModel, Field


class WalletBase(BaseModel):
    user_id: int = Field(..., example=123)
    currency: str = Field("USD", example="USD")


class WalletCreate(WalletBase):
    pass


class WalletRead(WalletBase):
    id: int
    balance: Decimal
    status: str

    class Config:
        orm_mode = True
