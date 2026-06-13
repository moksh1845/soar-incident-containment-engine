import requests

WAZUH_URL = "https://192.168.56.107:55000"
USERNAME = "wazuh-wui"
PASSWORD = "dd+7M?OJZ81rw2*cyZ8FhWRJvk588hE."


class WazuhClient:

    def get_token(self):

        response = requests.get(
            f"{WAZUH_URL}/security/user/authenticate?raw=true",
            auth=(USERNAME, PASSWORD),
            verify=False
        )

        response.raise_for_status()

        return response.text

    def get_alerts(self):

        token = self.get_token()

        headers = {
            "Authorization": f"Bearer {token}"
        }

        response = requests.get(
            f"{WAZUH_URL}/alerts",
            headers=headers,
            verify=False
        )

        response.raise_for_status()

        return response.json()