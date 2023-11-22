#!/usr/bin/python3

"""Simple CLI password manager tool."""


import sys


import add_password


def search_password() -> None:
    print("search password")


def delete_password() -> None:
    print("delete password")


def list_password() -> None:
    print("list password")


def help() -> None:
    print("Pyssword Manager")
    print("Available options:")
    print("     add / a:        add a password")
    print("     delete / d:     delete a password")
    print("     list / l:       list available information")
    print("     search / s:     search for password information")
    print("     help / h:       list this help menu")


def handle_command(command: str) -> None:
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
        help()
        return

    print("Command not recognised. Type help or h for help menu.")
    return


def main():
    print("Pyssword Manager")
    while True:
        command = input("Enter command: ")
        handle_command(command)


if __name__ == "__main__":
    main()
