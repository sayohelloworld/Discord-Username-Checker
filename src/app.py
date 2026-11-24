import os
import sys
import time

from .checker import check_user
from .validator import validate_username

VERSION = "1.0.0"
AUTHOR = "Sayonara"


def clear():
    os.system("cls")


def banner():
    print(r"""
 ____  _                       _
|  _ \(_)___  ___ ___  _ __ __| |
| | | | / __|/ __/ _ \| '__/ _` |
| |_| | \__ \ (_| (_) | | | (_| |
|____/|_|___/\___\___/|_|  \__,_|

       DISCORD USERNAME CHECKER
""")
    print(f"       Version {VERSION}")
    print(f"       Developed by {AUTHOR}")
    print("=" * 50)


def credits():
    clear()
    banner()

    print("\nCREDITS")
    print("-" * 50)
    print(f"Project      : Discord Username Checker")
    print(f"Developer    : {AUTHOR}")
    print(f"Version      : {VERSION}")
    print("Language     : Python")
    print("HTTP Library : Requests")
    print("-" * 50)

    input("\nPress ENTER to return...")


def check_single():
    clear()
    banner()

    username = input("\nEnter a username: ").strip()

    if not validate_username(username):
        print("\n[INVALID] Invalid username format.")
        input("\nPress ENTER to continue...")
        return

    print("\nChecking username...")

    result = check_user(username)

    print(f"\n[{result}] @{username}")
    input("\nPress ENTER to continue...")


def check_multiple():
    clear()
    banner()

    raw = input("\nEnter usernames separated by commas: ")

    usernames = [
        username.strip()
        for username in raw.split(",")
        if username.strip()
    ]

    if not usernames:
        print("\n[!] No usernames provided.")
        input("\nPress ENTER to continue...")
        return

    print(f"\nChecking {len(usernames)} usernames...\n")

    for username in usernames:
        if not validate_username(username):
            print(f"[INVALID] @{username}")
            continue

        result = check_user(username)
        print(f"[{result}] @{username}")

        if result == "RATE LIMITED":
            print("\n[!] Discord rate limit reached.")
            break

        time.sleep(2)

    input("\nPress ENTER to continue...")


def main_menu():
    while True:
        clear()
        banner()

        print("\n[1] Check a username")
        print("[2] Check multiple usernames")
        print("[3] Credits")
        print("[4] Exit")

        choice = input("\nSelect an option: ").strip()

        if choice == "1":
            check_single()

        elif choice == "2":
            check_multiple()

        elif choice == "3":
            credits()

        elif choice == "4":
            print("\nThank you for using Discord Username Checker.")
            time.sleep(1)
            break

        else:
            print("\n[!] Invalid option.")
            time.sleep(1)


if __name__ == "__main__":
    try:
        main_menu()
    except KeyboardInterrupt:
        print("\nApplication interrupted.")
        input("Press ENTER to close...")
    except Exception as error:
        print(f"\n[FATAL ERROR] {error}")
        input("\nPress ENTER to close...")
