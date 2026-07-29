from fastapi import APIRouter
from .service import check_health
from .models import HealthResponse

router = APIRouter()


@router.get("/health", response_model=HealthResponse)
def health_check():
    return check_health()