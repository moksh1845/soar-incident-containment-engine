from pydantic import BaseModel
from typing import Optional


class WazuhWebhook(BaseModel):

    rule_id: Optional[int] = None

    agent_id: Optional[str] = None

    agent_name: Optional[str] = None

    level: Optional[int] = None

    title: Optional[str] = None

    description: Optional[str] = None

    src_ip: Optional[str] = None

    raw_alert: dict