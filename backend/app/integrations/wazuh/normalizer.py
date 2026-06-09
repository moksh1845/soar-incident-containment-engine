class WazuhNormalizer:

    @staticmethod
    def normalize(payload: dict):

        return {
            "wazuh_rule_id": payload.get(
                "rule_id",
                0
            ),

            "agent_id": payload.get(
                "agent_id",
                "unknown"
            ),

            "agent_name": payload.get(
                "agent_name",
                "unknown"
            ),

            "severity": payload.get(
                "severity",
                0
            ),

            "title": payload.get(
                "title",
                "Unknown Alert"
            ),

            "description": payload.get(
                "description",
                ""
            ),

            "src_ip": payload.get(
                "src_ip"
            ),

            "status": "OPEN",

            "raw_alert": payload
        }