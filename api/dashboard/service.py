from .models import DashboardResponse

from api.machines.service import get_machines
from api.alerts.service import get_active_alerts


def get_dashboard() -> DashboardResponse:
    """
    Builds the complete dashboard response by combining
    machine status, active alerts and summary indicators.
    """

    # Retrieve current plant status.
    machines = get_machines()
    # Calculate dashboard statistics.
    active_alerts = get_active_alerts()
    # Calculate dashboard statistics.
    total_machines = len(machines)

    normal_machines = 0
    warning_machines = 0
    critical_machines = 0

    for machine in machines:

        if machine.health == "NORMAL":
            normal_machines += 1

        elif machine.health == "WARNING":
            warning_machines += 1

        elif machine.health == "CRITICAL":
            critical_machines += 1
            
    # Build dashboard response.
    return DashboardResponse(
        total_machines=total_machines,
        normal_machines=normal_machines,
        warning_machines=warning_machines,
        critical_machines=critical_machines,
        machines=machines,
        active_alerts=active_alerts,
    )

