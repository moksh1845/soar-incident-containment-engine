from uuid import UUID

from pydantic import BaseModel
from pydantic import ConfigDict
from pydantic import EmailStr


class UserCreate(BaseModel):

    username: str

    email: EmailStr

    password: str

    role_id: UUID


class UserResponse(BaseModel):

    id: UUID

    username: str

    email: EmailStr

    is_active: bool

    role_id: UUID

    model_config = ConfigDict(
        from_attributes=True
    )