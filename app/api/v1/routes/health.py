import logging
from fastapi import APIRouter

router = APIRouter()
logger = logging.getLogger(__name__)


@router.get("/health", summary="Service health check")
def health_check():
    logger.info("Health check requested")
    return {
        "service": "rootlender-wallet-service",
        "status": "ok",
    }
