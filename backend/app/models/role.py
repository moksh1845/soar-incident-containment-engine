import uuid

from sqlalchemy import Column
from sqlalchemy import String

from sqlalchemy.dialects.postgresql import UUID

from app.database.base import Base


class Role(Base):

    __tablename__ = "roles"

    id = Column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4
    )

    name = Column(
        String(50),
        unique=True,
        nullable=False
    )