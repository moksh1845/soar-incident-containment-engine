class WazuhNormalizer:

    @staticmethod
    def normalize(alert_data):

        return {

            "wazuh_rule_id": alert_data.get(
                "rule_id",
                0
            ),

            "agent_id": alert_data.get(
                "agent_id",
                "unknown"
            ),

            "agent_name": alert_data.get(
                "agent_name",
                "unknown"
            ),

            "severity": alert_data.get(
                "level",
                0
            ),

            "title": alert_data.get(
                "title",
                "Unknown Alert"
            ),

            "description": alert_data.get(
                "description",
                ""
            ),

            "src_ip": alert_data.get(
                "src_ip",
                ""
            ),

            "status": "OPEN",

            "raw_alert": alert_data
        }