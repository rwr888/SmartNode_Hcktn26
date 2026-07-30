from fastapi import APIRouter
from .service import get_machines
from .models import MachineResponse

router = APIRouter()

@router.get("/machines", response_model=list[MachineResponse])
def machines():
    return get_machines()