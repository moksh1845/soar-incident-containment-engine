import requests


class WazuhClient:

    @staticmethod
    def health():

        try:

            response = requests.get(
                "http://localhost:55000",
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