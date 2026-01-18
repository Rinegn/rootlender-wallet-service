from fastapi import APIRouter, HTTPException

router = APIRouter(
    prefix="/wallet/transactions",
    tags=["wallet-transactions"],
)

@router.post("/purchase")
def purchase():
    raise HTTPException(
        status_code=501,
        detail="Purchase temporarily disabled (Phase 6C complete, Phase 7 pending)",
    )
