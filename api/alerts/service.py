from datetime import datetime

from api.rules.models import RuleResult
from .models import AlertResponse

from api.database.connection import db
from api.database.config import ALERTS_COLLECTION


def create_alert(rule: RuleResult) -> AlertResponse:

    existing = db[ALERTS_COLLECTION].find_one(
        {
            "machine_id": rule.machine_id,
            "health": rule.health,
            "diagnostic": rule.diagnostic,
            "acknowledged": False,
        }
    )

    if existing:
        existing.pop("_id", None)
        return AlertResponse(**existing)

    alert = AlertResponse(
        machine_id=rule.machine_id,
        health=rule.health,
        diagnostic=rule.diagnostic,
        recommendation=rule.recommendation,
        acknowledged=False,
        timestamp=datetime.now().isoformat(),
    )

    db[ALERTS_COLLECTION].insert_one(
        alert.model_dump()
    )

    return alert

def get_alerts() -> list[AlertResponse]:

    alerts = []

    cursor = db[ALERTS_COLLECTION].find()

    for document in cursor:

        document.pop("_id", None)

        alerts.append(
            AlertResponse(**document)
        )

    return alerts

def get_active_alerts() -> list[AlertResponse]:

    alerts = []

    cursor = db[ALERTS_COLLECTION].find(
        {
            "acknowledged": False
        }
    )

    for document in cursor:

        document.pop("_id", None)

        alerts.append(
            AlertResponse(**document)
        )

    return alerts

def acknowledge_alert(machine_id: str):

    db[ALERTS_COLLECTION].update_many(
        {
            "machine_id": machine_id,
            "acknowledged": False
        },
        {
            "$set": {
                "acknowledged": True
            }
        }
    )


