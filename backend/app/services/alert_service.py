from fastapi import HTTPException
from fastapi import status

from sqlalchemy.orm import Session

from app.models.alert import Alert

from app.schemas.alert import AlertCreate

from app.repositories.alert_repository import AlertRepository


class AlertService:

    @staticmethod
    def create_alert(
        db: Session,
        alert_data: AlertCreate
    ):

        alert = Alert(
            wazuh_rule_id=alert_data.wazuh_rule_id,
            agent_id=alert_data.agent_id,
            agent_name=alert_data.agent_name,
            severity=alert_data.severity,
            title=alert_data.title,
            description=alert_data.description,
            src_ip=alert_data.src_ip,
            status=alert_data.status,
            raw_alert=alert_data.raw_alert
        )

        return AlertRepository.create_alert(
            db,
            alert
        )

    @staticmethod
    def get_alert(
        db: Session,
        alert_id
    ):

        alert = AlertRepository.get_alert_by_id(
            db,
            alert_id
        )

        if not alert:

            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Alert not found"
            )

        return alert

    @staticmethod
    def get_all_alerts(
        db: Session
    ):

        return AlertRepository.get_all_alerts(
            db
        )