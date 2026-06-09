from fastapi import APIRouter
from fastapi import Depends

from sqlalchemy.orm import Session

from app.database.session import get_db

from app.schemas.wazuh import WazuhWebhook
from app.schemas.alert import AlertCreate

from app.services.alert_service import AlertService

from app.integrations.wazuh.normalizer import (
    WazuhNormalizer
)

from app.integrations.wazuh.client import (
    WazuhClient
)

router = APIRouter(
    prefix="/wazuh",
    tags=["Wazuh"]
)


@router.get("/health")
def health():

    return WazuhClient.health()


@router.post("/webhook")
def receive_alert(
    payload: WazuhWebhook,
    db: Session = Depends(get_db)
):

    normalized = (
        WazuhNormalizer.normalize(
            payload.model_dump()
        )
    )

    alert = AlertCreate(
        **normalized
    )

    AlertService.create_alert(
        db,
        alert
    )

    return {
        "message": "Alert received successfully"
    }