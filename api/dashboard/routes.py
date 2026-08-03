from fastapi import APIRouter

from .service import get_dashboard
from .models import DashboardResponse

router = APIRouter()


@router.get("/dashboard", response_model=DashboardResponse)
def dashboard():
    return get_dashboard()