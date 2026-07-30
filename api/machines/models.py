from pydantic import BaseModel

class MachineResponse(BaseModel):
    machine_id: str
    status: str
    temperature: float
    vibration: float
    current: float