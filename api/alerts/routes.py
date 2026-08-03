from fastapi import APIRouter

from .service import (
    get_alerts,
    get_active_alerts,
    acknowledge_alert,
)
from .models import AlertResponse

router = APIRouter()


@router.get("/alerts", response_model=list[AlertResponse])
def alerts():

    return get_alerts()


@router.get("/alerts/active", response_model=list[AlertResponse])
def active_alerts():

    return get_active_alerts()

@router.put("/alerts/{machine_id}/acknowledge")
def acknowledge(machine_id: str):

    acknowledge_alert(machine_id)

    return {
        "message": f"Alerts from {machine_id} acknowledged."
    }

