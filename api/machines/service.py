import random

from .models import MachineResponse, MachineStatusResponse

from api.database.connection import db
from api.database.config import MACHINES_COLLECTION

from api.rules.service import evaluate_machine
from api.alerts.service import create_alert


def build_machine(machine_id: str, status: str):
    """
    Generates simulated sensor values for one machine,
    evaluates its health, stores the latest state in MongoDB,
    creates an alert if necessary and returns both the machine
    and the evaluated rule.
    """

    # Generate realistic sensor values according to machine status.
    if status == "running":
        temperature = round(random.uniform(45, 75), 1)
        vibration = round(random.uniform(0.20, 0.80), 2)
        current = round(random.uniform(4.0, 8.0), 2)

    elif status == "idle":
        temperature = round(random.uniform(25, 40), 1)
        vibration = round(random.uniform(0.01, 0.08), 2)
        current = round(random.uniform(0.2, 1.0), 2)

    elif status == "warning":
        temperature = round(random.uniform(75, 90), 1)
        vibration = round(random.uniform(0.80, 1.20), 2)
        current = round(random.uniform(8.0, 10.0), 2)

    else:  # fault
        temperature = round(random.uniform(90, 110), 1)
        vibration = round(random.uniform(1.20, 2.00), 2)
        current = round(random.uniform(10.0, 15.0), 2)

    # Build the machine object.
    machine = MachineResponse(
        machine_id=machine_id,
        status=status,
        temperature=temperature,
        vibration=vibration,
        current=current,
    )

    # Evaluate machine health using the Rules Engine.
    rule = evaluate_machine(machine)

    # Generate an alert if this condition is not already active.
    create_alert(rule)

    # Store only the latest machine state.
    document = {
        "machine_id": machine.machine_id,
        "status": machine.status,
        "health": rule.health,
        "temperature": machine.temperature,
        "vibration": machine.vibration,
        "current": machine.current,
        "diagnostic": rule.diagnostic,
        "recommendation": rule.recommendation,
        "timestamp": rule.timestamp,
    }

    db[MACHINES_COLLECTION].update_one(
        {"machine_id": machine.machine_id},
        {"$set": document},
        upsert=True,
    )

    return machine, rule


def get_machines() -> list[MachineStatusResponse]:
    """
    Generates the simulated plant state and returns the
    evaluated status of every machine.
    """

    data = [
        build_machine("motor_01", "running"),
        build_machine("pump_01", "running"),
        build_machine("compressor_01", "idle"),
    ]

    result = []

    for machine, rule in data:

        result.append(
            MachineStatusResponse(
                machine_id=machine.machine_id,
                status=machine.status,
                health=rule.health,
                temperature=machine.temperature,
                vibration=machine.vibration,
                current=machine.current,
                diagnostic=rule.diagnostic,
                recommendation=rule.recommendation,
                timestamp=rule.timestamp,
            )
        )

    return result

