from fastapi import APIRouter
from fastapi import Depends

from sqlalchemy.orm import Session

from app.database.session import get_db

from app.schemas.wazuh import WazuhWebhook
from app.schemas.alert import AlertCreate

from app.services.alert_service import AlertService
from app.services.wazuh_service import WazuhService

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

wazuh_service = WazuhService()


@router.get("/health")
def health():

    return WazuhClient.health()


@router.get("/agents")
def get_agents():

    return wazuh_service.get_agents()


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


@router.post("/import-agent/{agent_id}")
def import_agent_alert(
    agent_id: str,
    db: Session = Depends(get_db)
):

    data = WazuhClient.get_agent_by_id(
        agent_id
    )

    if not data:

        return {
            "message": "Agent not found"
        }

    affected_item = data

    alert = AlertCreate(

        wazuh_rule_id=9999,

        agent_id=str(
            affected_item.get(
                "id",
                agent_id
            )
        ),

        agent_name=affected_item.get(
            "name",
            "Unknown Agent"
        ),

        severity=5,

        title="Agent Imported",

        description=(
            "Imported from Wazuh API"
        ),

        src_ip=affected_item.get(
            "ip",
            ""
        ),

        status="OPEN",

        raw_alert=affected_item
    )

    AlertService.create_alert(
        db,
        alert
    )

    return {
        "message": "Imported successfully",
        "agent_name": affected_item.get(
            "name"
        ),
        "agent_id": affected_item.get(
            "id"
        )
    }