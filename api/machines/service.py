import random

from .models import MachineResponse


def get_machines():
    return [
        MachineResponse(
            machine_id="motor_01",
            status="running",
            temperature=round(random.uniform(35, 75), 1),
            vibration=round(random.uniform(0.05, 0.80), 2),
            current=round(random.uniform(2.0, 8.0), 2)
        ),
        MachineResponse(
            machine_id="pump_01",
            status="running",
            temperature=round(random.uniform(35, 75), 1),
            vibration=round(random.uniform(0.05, 0.80), 2),
            current=round(random.uniform(2.0, 8.0), 2)
        ),
        MachineResponse(
            machine_id="compressor_01",
            status="idle",
            temperature=round(random.uniform(35, 75), 1),
            vibration=round(random.uniform(0.05, 0.80), 2),
            current=round(random.uniform(2.0, 8.0), 2)
        )
    ]