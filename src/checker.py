import requests

API_URL = (
    "https://discord.com/api/v9/"
    "unique-username/username-attempt-unauthed"
)

session = requests.Session()


def check_user(username):
    username = username.strip().removeprefix("@")

    try:
        response = session.post(
            API_URL,
            json={"username": username},
            timeout=10
        )

        if response.status_code == 429:
            return "RATE LIMITED"

        if response.status_code != 200:
            return f"ERROR HTTP {response.status_code}"

        data = response.json()

        if data.get("taken") is True:
            return "TAKEN"

        if data.get("taken") is False:
            return "AVAILABLE"

        return "UNKNOWN"

    except requests.RequestException:
        return "CONNECTION ERROR"

    except ValueError:
        return "INVALID RESPONSE"