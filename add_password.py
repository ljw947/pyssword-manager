"""Add password information"""

import getpass

DEFAULT_FIELDS = [
    "username",
    "password"
]

def add_password() -> None:
    print("\nAdding password.")
    print("Default fields are", *DEFAULT_FIELDS)
    default = input("Use default fields? Y/N: ")
    if default.lower() in ("yes", "y"):
        _add_password_default_fields()


def _add_password_default_fields() -> None:
    username = input(f"{DEFAULT_FIELDS[0]}: ")
    password = getpass.getpass()
