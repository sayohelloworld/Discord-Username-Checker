import re


def validate_username(username):
    username = username.strip().removeprefix("@")

    if not 2 <= len(username) <= 32:
        return False

    if not re.fullmatch(r"[a-z0-9._]+", username):
        return False

    if username.startswith(".") or username.endswith("."):
        return False

    if ".." in username:
        return False

    return True