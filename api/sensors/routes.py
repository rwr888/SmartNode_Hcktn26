from fastapi import APIRouter
from .service import get_sensors
from .models import SensorResponse

router = APIRouter()


@router.get("/sensors", response_model=list[SensorResponse])
def sensors():
    return get_sensors()
