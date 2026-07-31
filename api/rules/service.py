from datetime import datetime

from api.machines.models import MachineResponse
from .models import RuleResult


def evaluate_machine(machine: MachineResponse) -> RuleResult:

    return RuleResult(
        machine_id=machine.machine_id,
        health="NORMAL",
        diagnostic="Normal operation",
        recommendation="Continue monitoring",
        timestamp=datetime.now().isoformat()
    )
