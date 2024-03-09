#!/usr/bin/python3

"""Simple CLI password manager tool."""


import sys

# local imports
from pyssword_lib import add_password, account


def search_password() -> None:
    """TODO: search for a password"""
    print("search password")


def delete_password() -> None:
    """TODO: delete a password"""
    print("delete password")


def list_password() -> None:
    """TODO: list passwords"""
    print("list password")


def print_help() -> None:
    """Print help menu"""
    print("Pyssword Manager")
    print("Available options:")
    print("     add / a:        add a password")
    print("     delete / d:     delete a password")
    print("     list / l:       list available information")
    print("     search / s:     search for password information")
    print("     help / h:       list this help menu")


def handle_command(command: str) -> None:
    """Handle command on CLI"""
    lower_command = command.lower()
    if lower_command in ("exit", "quit", "q"):
        print("Exiting.")
        sys.exit(0)

    if lower_command in ("add", "a"):
        add_password.add_password()
        return

    if lower_command in ("search", "s"):
        search_password()
        return

    if lower_command in ("delete", "d"):
        delete_password()
        return

    if lower_command in ("list", "l"):
        list_password()
        return

    if lower_command in ("help", "h"):
        print_help()
        return

    print("Command not recognised. Type help or h for help menu.")
    return


def main() -> None:
    """Main function, controls logic flow of application."""
    print("Pyssword Manager")
    accounts = account.Accounts()

    accounts.add_table()
    accounts.add_value()
    accounts.get_table()

    while True:
        command = input("Enter command: ")
        handle_command(command)


if __name__ == "__main__":
    main()
