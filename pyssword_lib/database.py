"""Database Handler"""

import logging

from pathlib import Path

import sqlite3

# TODO: change
DEFAULT_DATABASE_PATH = Path.cwd() / "test"


class Database():
    """
    Base class representing a sqlite3 database object.
    Derived classes will extend it when instantiated.
    """
    def __init__(self):
        self.database_name = None
        self.database_path = None
        self.sqlite_connection = None

    def check_database(self) -> bool:
        """Check if given database is initialised. If it is, try and unlock it."""
        if not Path.exists(self.database_path):
            logging.debug("%s database does not exist.", self.database_name)
            return False
        return True

    def setup_database_path(self) -> None:
        """Helper method to set up path to database file."""
        self.database_path = DEFAULT_DATABASE_PATH / f"{self.database_name}.db"

    def create_database_path(self) -> None:
        """Create the database on disk if not already created."""
        if not Path.exists(DEFAULT_DATABASE_PATH):
            Path.mkdir(DEFAULT_DATABASE_PATH, parents=True)

    def initialise_database_file(self) -> sqlite3.Connection:
        """Initialise database for usage."""
        try:
            self.setup_database_path()
            self.create_database_path()
            connection = sqlite3.connect(self.database_path)
        except Exception as error:  # TODO: no broad except
            logging.error(f"Unable to create database storage at {DEFAULT_DATABASE_PATH}, %s.", error)

        self.sqlite_connection = connection
