from fastapi import FastAPI

from api.health.routes import router as health_router
from api.sensors.routes import router as sensors_router
from api.machines.routes import router as machines_router
from api.alerts.routes import router as alerts_router
from api.dashboard.routes import router as dashboard_router

from api.database.connection import db

app = FastAPI()

app.include_router(health_router)
app.include_router(sensors_router)
app.include_router(machines_router)
app.include_router(alerts_router)
app.include_router(dashboard_router)

