from pydantic import BaseModel


class MachineResponse(BaseModel):
    machine_id: str
    status: str
    temperature: float
    vibration: float
    current: float


class MachineStatusResponse(BaseModel):
    machine_id: str
    status: str

    health: str

    temperature: float
    vibration: float
    current: float

    diagnostic: str
    recommendation: str
    timestamp: str