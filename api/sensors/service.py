from .models import SensorResponse


def get_sensors():
    return [
        SensorResponse(
            id="temp_01",
            type="temperature",
            value=24.8,
            unit="°C"
        )
    ]