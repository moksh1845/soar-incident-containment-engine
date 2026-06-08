from uuid import UUID

from fastapi import APIRouter
from fastapi import Depends

from sqlalchemy.orm import Session

from app.database.session import get_db

from app.schemas.alert import AlertCreate
from app.schemas.alert import AlertResponse

from app.services.alert_service import AlertService

router = APIRouter(
    prefix="/alerts",
    tags=["Alerts"]
)


@router.post(
    "",
    response_model=AlertResponse
)
def create_alert(
    alert_data: AlertCreate,
    db: Session = Depends(get_db)
):

    return AlertService.create_alert(
        db,
        alert_data
    )


@router.get(
    "",
    response_model=list[AlertResponse]
)
def get_alerts(
    db: Session = Depends(get_db)
):

    return AlertService.get_all_alerts(
        db
    )


@router.get(
    "/{alert_id}",
    response_model=AlertResponse
)
def get_alert(
    alert_id: UUID,
    db: Session = Depends(get_db)
):

    return AlertService.get_alert(
        db,
        alert_id
    )