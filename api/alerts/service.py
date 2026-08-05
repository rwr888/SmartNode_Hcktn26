from datetime import datetime

from api.rules.models import RuleResult
from .models import AlertResponse

from api.database.connection import db
from api.database.config import ALERTS_COLLECTION


def create_alert(rule: RuleResult) -> AlertResponse:
    """
    Creates a new alert if an equivalent active alert
    does not already exist.
    """

    # Prevent duplicated active alerts.
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

    # Build alert object.
    alert = AlertResponse(
        machine_id=rule.machine_id,
        health=rule.health,
        diagnostic=rule.diagnostic,
        recommendation=rule.recommendation,
        acknowledged=False,
        timestamp=datetime.now().isoformat(),
    )

    # Store alert in MongoDB.
    db[ALERTS_COLLECTION].insert_one(
        alert.model_dump()
    )

    return alert


def get_alerts() -> list[AlertResponse]:
    """
    Returns every alert stored in the database.
    """

    alerts = []

    cursor = db[ALERTS_COLLECTION].find()

    for document in cursor:

        document.pop("_id", None)

        alerts.append(
            AlertResponse(**document)
        )

    return alerts


def get_active_alerts() -> list[AlertResponse]:
    """
    Returns only alerts that have not been acknowledged.
    """

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
    """
    Marks every active alert of a machine as acknowledged.
    """

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


