from pydantic import BaseModel


class RuleResult(BaseModel):
    machine_id: str
    health: str
    diagnostic: str
    recommendation: str
    timestamp: str

    