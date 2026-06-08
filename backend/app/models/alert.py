import uuid

from sqlalchemy import Column
from sqlalchemy import String
from sqlalchemy import Integer
from sqlalchemy import DateTime
from sqlalchemy import JSON
from sqlalchemy import Text

from sqlalchemy.dialects.postgresql import UUID

from datetime import datetime

from app.database.base import Base


class Alert(Base):

    __tablename__ = "alerts"

    id = Column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4
    )

    wazuh_rule_id = Column(
        Integer,
        nullable=False
    )

    agent_id = Column(
        String(50),
        nullable=False
    )

    agent_name = Column(
        String(100),
        nullable=False
    )

    severity = Column(
        Integer,
        nullable=False
    )

    title = Column(
        String(255),
        nullable=False
    )

    description = Column(
        Text,
        nullable=False
    )

    src_ip = Column(
        String(100),
        nullable=True
    )

    status = Column(
        String(50),
        default="OPEN"
    )

    raw_alert = Column(
        JSON,
        nullable=True
    )

    created_at = Column(
        DateTime,
        default=datetime.utcnow
    )