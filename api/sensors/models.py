from pydantic import BaseModel


class SensorResponse(BaseModel):
    id: str
    type: str
    value: float
    unit: str