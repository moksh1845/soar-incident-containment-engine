from sqlalchemy.orm import Session

from app.models.alert import Alert


class AlertRepository:

    @staticmethod
    def create_alert(
        db: Session,
        alert: Alert
    ):

        db.add(alert)

        db.commit()

        db.refresh(alert)

        return alert

    @staticmethod
    def get_alert_by_id(
        db: Session,
        alert_id
    ):

        return (
            db.query(Alert)
            .filter(Alert.id == alert_id)
            .first()
        )

    @staticmethod
    def get_all_alerts(
        db: Session
    ):

        return (
            db.query(Alert)
            .order_by(Alert.created_at.desc())
            .all()
        )