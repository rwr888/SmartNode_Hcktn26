import random

from .models import MachineResponse
from api.database.connection import db
from api.database.config import MACHINES_COLLECTION


def build_machine(machine_id: str, status: str) -> MachineResponse:

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

    machine = MachineResponse(
        machine_id=machine_id,
        status=status,
        temperature=temperature,
        vibration=vibration,
        current=current,
    )

    db[MACHINES_COLLECTION].insert_one(machine.model_dump())

    return machine


def get_machines():
    return [
        build_machine("motor_01", "running"),
        build_machine("pump_01", "running"),
        build_machine("compressor_01", "idle"),
    ]

