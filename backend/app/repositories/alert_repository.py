from sqlalchemy.orm import Session
from app.models.alert import Alert
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
    
        @staticmethod
        def get_open_alerts(
        db
    ):

            return (
            db.query(Alert)
            .filter(Alert.status == "OPEN")
            .all()
        )

    @staticmethod
    def get_critical_alerts(
        db
    ):

        return (
            db.query(Alert)
            .filter(Alert.severity >= 10)
            .all()
        )

    @staticmethod
    def get_alert_statistics(
        db
    ):

        total_alerts = (
            db.query(Alert)
            .count()
        )

        open_alerts = (
            db.query(Alert)
            .filter(Alert.status == "OPEN")
            .count()
        )

        critical_alerts = (
            db.query(Alert)
            .filter(Alert.severity >= 10)
            .count()
        )

        return {
            "total_alerts": total_alerts,
            "open_alerts": open_alerts,
            "critical_alerts": critical_alerts
        }