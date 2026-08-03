from pydantic import BaseModel

from api.machines.models import MachineStatusResponse
from api.alerts.models import AlertResponse


class DashboardResponse(BaseModel):

    total_machines: int

    normal_machines: int
    warning_machines: int
    critical_machines: int

    machines: list[MachineStatusResponse]

    active_alerts: list[AlertResponse]

