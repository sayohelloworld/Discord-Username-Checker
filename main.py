import os
import subprocess
import sys

PROJECT_DIR = os.path.dirname(os.path.abspath(__file__))
APP_FILE = os.path.join(PROJECT_DIR, "src", "app.py")


def main():
    if os.name != "nt":
        print("This application requires Windows.")
        return

    subprocess.Popen(
        [
            "cmd.exe",
            "/k",
            f'"{sys.executable}" "{APP_FILE}"'
        ],
        cwd=PROJECT_DIR,
        creationflags=subprocess.CREATE_NEW_CONSOLE
    )


if __name__ == "__main__":
    main()