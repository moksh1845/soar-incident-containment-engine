from app.integrations.wazuh.client import (
    WazuhClient
)


class WazuhService:

    @staticmethod
    def get_agents():

        return WazuhClient.get_agents()
    @staticmethod
    def get_alerts():

        return WazuhClient.get_alerts()