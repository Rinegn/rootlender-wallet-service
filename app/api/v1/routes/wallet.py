from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.db import get_db
from app.schemas.wallet import WalletCreate, WalletRead
from app.services.wallet_service import WalletService

router = APIRouter()


@router.post(
    "/wallets",
    response_model=WalletRead,
    status_code=status.HTTP_201_CREATED,
    summary="Create a wallet for a user",
)
def create_wallet(
    payload: WalletCreate,
    db: Session = Depends(get_db),
):
    existing = WalletService.get_wallet_by_user_id(
        db=db,
        user_id=payload.user_id,
        currency=payload.currency,
    )

    if existing:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Wallet already exists for this user and currency",
        )

    wallet = WalletService.create_wallet(
        db=db,
        user_id=payload.user_id,
        currency=payload.currency,
    )

    return wallet


@router.get(
    "/wallets/{wallet_id}",
    response_model=WalletRead,
    summary="Get a wallet by ID",
)
def get_wallet(
    wallet_id: int,
    db: Session = Depends(get_db),
):
    wallet = WalletService.get_wallet_by_id(db=db, wallet_id=wallet_id)

    if not wallet:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Wallet not found",
        )

    return wallet
