from pydantic import BaseModel


class AlertResponse(BaseModel):
    machine_id: str

    health: str

    title: str

    message: str

    acknowledged: bool

    timestamp: str


    