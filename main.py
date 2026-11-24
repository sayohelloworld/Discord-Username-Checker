
import os
import subprocess
import sys

PROJECT_DIR = os.path.dirname(os.path.abspath(__file__))


def main():
    if os.name != "nt":
        raise OSError("Windows is required.")

    subprocess.Popen(
        [
            sys.executable,
            "-u",
            "-m",
            "src.app"
        ],
        cwd=PROJECT_DIR,
        creationflags=subprocess.CREATE_NEW_CONSOLE
    )


if __name__ == "__main__":
    main()
