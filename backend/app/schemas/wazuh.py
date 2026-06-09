from pydantic import BaseModel


class WazuhWebhook(BaseModel):

    rule_id: int

    severity: int

    title: str

    description: str

    src_ip: str | None = None

    agent_id: str

    agent_name: str