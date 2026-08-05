from datetime import datetime

from api.machines.models import MachineResponse
from .models import RuleResult


"""Classifies machine temperature into severity levels."""
def classify_temperature(value: float) -> str:
    if value < 45:
        return "LOW"
    elif value < 75:
        return "NORMAL"
    elif value < 90:
        return "HIGH"
    else:
        return "CRITICAL"


"""Classifies vibration level."""
def classify_vibration(value: float) -> str:
    if value < 0.10:
        return "LOW"
    elif value < 0.60:
        return "NORMAL"
    elif value < 1.20:
        return "HIGH"
    else:
        return "CRITICAL"


def classify_current(value: float) -> str:
    """Classifies electrical current."""
    if value < 1.0:
        return "LOW"
    elif value < 6.0:
        return "NORMAL"
    elif value < 9.0:
        return "HIGH"
    else:
        return "CRITICAL"


"""
Evaluates machine sensor values using the SmartNode
rule engine and returns its health assessment.
"""
def evaluate_machine(machine: MachineResponse) -> RuleResult:

    temperature = classify_temperature(machine.temperature)
    vibration = classify_vibration(machine.vibration)
    current = classify_current(machine.current)

    health = "NORMAL"
    diagnostic = "Normal operation"
    recommendation = "Continue monitoring."

    # R-012
    # -------------------------
    # Critical conditions
    # -------------------------
    if temperature == "CRITICAL":
        health = "CRITICAL"
        diagnostic = "Possible winding insulation failure or severe overheating."
        recommendation = "Stop machine immediately."

    # R-009
    elif vibration == "CRITICAL":
        health = "CRITICAL"
        diagnostic = "Excessive vibration detected."
        recommendation = "Inspect rotating components immediately."

    # R-004
    elif (
        machine.status == "running"
        and temperature == "HIGH"
        and vibration == "HIGH"
        and current == "HIGH"
    ):
        health = "CRITICAL"
        diagnostic = "Possible mechanical failure."
        recommendation = "Stop machine and perform inspection."

    # R-003
    # -------------------------
    # Warning conditions
    # -------------------------
    elif (
        machine.status == "running"
        and temperature == "HIGH"
        and vibration == "HIGH"
    ):
        health = "WARNING"
        diagnostic = "Possible bearing wear."
        recommendation = "Inspect bearings."

    # R-008
    elif (
        machine.status == "running"
        and vibration == "HIGH"
    ):
        health = "WARNING"
        diagnostic = "Possible shaft misalignment."
        recommendation = "Check coupling alignment."

    # R-007
    elif (
        machine.status == "running"
        and current == "HIGH"
    ):
        health = "WARNING"
        diagnostic = "Electrical overload detected."
        recommendation = "Inspect electrical system."

    # R-006
    elif (
        machine.status == "idle"
        and temperature == "HIGH"
    ):
        health = "WARNING"
        diagnostic = "Machine heating while idle."
        recommendation = "Inspect cooling system."

    # R-011
    elif (
        machine.status == "idle"
        and current == "HIGH"
    ):
        health = "WARNING"
        diagnostic = "Unexpected current draw."
        recommendation = "Inspect electrical contactors."

    # -------------------------
    # Attention conditions
    # -------------------------
    # R-002
    elif (
        machine.status == "running"
        and temperature == "HIGH"
        and current == "HIGH"
    ):
        health = "ATTENTION"
        diagnostic = "Possible overload."
        recommendation = "Reduce load and continue monitoring."

    return RuleResult(
        machine_id=machine.machine_id,
        health=health,
        diagnostic=diagnostic,
        recommendation=recommendation,
        timestamp=datetime.now().isoformat()
    )

