from fastapi import FastAPI
from app.api.auth import router as auth_router
from app.database.base import Base
from app.database.session import engine
from app.api.alerts import router as alert_router
from app.api.wazuh import router as wazuh_router
import app.models


Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="SOAR Incident Containment Engine"
)
app.include_router(auth_router)
app.include_router(alert_router)
app.include_router(wazuh_router)

@app.get("/")
def root():
    return {
        "message": "SOAR Backend Running"
    }