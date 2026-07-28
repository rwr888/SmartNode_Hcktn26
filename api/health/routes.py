from fastapi import APIRouter
from .service import check_health

router = APIRouter()


@router.get("/health")
def health_check():
    return check_health()