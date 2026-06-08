from uuid import UUID

from pydantic import BaseModel
from pydantic import ConfigDict

from datetime import datetime


class AlertCreate(BaseModel):

    wazuh_rule_id: int

    agent_id: str

    agent_name: str

    severity: int

    title: str

    description: str

    src_ip: str | None = None

    status: str = "OPEN"

    raw_alert: dict | None = None


class AlertResponse(BaseModel):

    id: UUID

    wazuh_rule_id: int

    agent_id: str

    agent_name: str

    severity: int

    title: str

    description: str

    src_ip: str | None

    status: str

    raw_alert: dict | None

    created_at: datetime

    model_config = ConfigDict(
        from_attributes=True
    )