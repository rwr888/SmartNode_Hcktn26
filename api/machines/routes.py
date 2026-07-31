from fastapi import APIRouter
from .service import get_machines
from .models import MachineResponse
from .models import MachineStatusResponse

router = APIRouter()

@router.get("/machines", response_model=list[MachineStatusResponse])
def machines():
    return get_machines()

