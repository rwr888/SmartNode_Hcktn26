from pydantic import BaseModel


class AlertResponse(BaseModel):
    machine_id: str

    health: str

    diagnostic: str

    recommendation: str

    acknowledged: bool

    timestamp: str


    