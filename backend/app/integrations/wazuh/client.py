import requests

requests.packages.urllib3.disable_warnings()

WAZUH_URL = "https://192.168.56.107:55000"

USERNAME = "wazuh-wui"
PASSWORD = "dd+7M?OJZ81rw2*cyZ8FhWRJvk588hE."


class WazuhClient:

    @staticmethod
    def health():

        try:

            response = requests.get(
                WAZUH_URL,
                verify=False,
                timeout=5
            )

            return {
                "status": "online",
                "code": response.status_code
            }

        except Exception as e:

            return {
                "status": "offline",
                "error": str(e)
            }

    @staticmethod
    def get_token():

        response = requests.get(
            f"{WAZUH_URL}/security/user/authenticate?raw=true",
            auth=(
                USERNAME,
                PASSWORD
            ),
            verify=False
        )

        response.raise_for_status()

        return response.text

    @staticmethod
    def get_agents():

        token = WazuhClient.get_token()

        response = requests.get(
            f"{WAZUH_URL}/agents",
            headers={
                "Authorization": f"Bearer {token}"
            },
            verify=False
        )

        response.raise_for_status()

        return response.json()

    @staticmethod
    def get_alerts():

        token = WazuhClient.get_token()

        response = requests.get(
            f"{WAZUH_URL}/security/events",
            headers={
                "Authorization": f"Bearer {token}"
            },
            verify=False
        )

        response.raise_for_status()

        return response.json()

    @staticmethod
    def get_agent_by_id(agent_id):

        token = WazuhClient.get_token()

        response = requests.get(
            f"{WAZUH_URL}/agents",
            headers={
                "Authorization": f"Bearer {token}"
            },
            verify=False
        )

        response.raise_for_status()

        data = response.json()

        agents = data["data"]["affected_items"]

        for agent in agents:

            if agent["id"] == str(agent_id):
                return agent

        return None