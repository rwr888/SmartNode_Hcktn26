from datetime import datetime

from api.rules.models import RuleResult
from .models import AlertResponse

from api.database.connection import db
from api.database.config import ALERTS_COLLECTION


def create_alert(rule: RuleResult) -> AlertResponse:
    print("Creating alert...")

    existing = db[ALERTS_COLLECTION].find_one(
        {
            "machine_id": rule.machine_id,
            "health": rule.health,
            "title": rule.diagnostic,
            "acknowledged": False,
        }
        
    )

    if existing:
        existing.pop("_id", None)
        return AlertResponse(**existing)

    alert = AlertResponse(
        machine_id=rule.machine_id,
        health=rule.health,
        title=rule.diagnostic,
        message=rule.recommendation,
        acknowledged=False,
        timestamp=datetime.now().isoformat(),
    )

    db[ALERTS_COLLECTION].insert_one(
        alert.model_dump()
    )

    return alert
