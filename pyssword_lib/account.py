"""Account database"""

import datetime

from pathlib import Path

from pyssword_lib.database import Database


class Accounts(Database):
    """Accounts class, handles user accounts"""
    def __init__(self, database_dir: Path = None):
        """
        Initiate the Accounts database.

        Args:
            database_dir (Path): will typically be None, argument used for unit tests.
        """
        Database.__init__(self, database_dir)
        self.database_name = "accounts"
        self.initialise_database_file()

    def add_table(self):
        """Sets up accounts table with relevant columns."""
        cursor = self.sqlite_connection.cursor()
        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS Accounts
            (
                Id integer PRIMARY KEY,
                Name text NOT NULL,
                Email text NOT NULL,
                MasterPassword text NOT NULL,
                PublicKey text NOT NULL,
                PrivateKey text NOT NULL,
                CreationDate integer NOT NULL,
                RevisionDate integer NOT NULL,
                DeletionDate integer
            )
            """
        )

    def add_value(self, id: str = None, field: str = None, value: str = None):
        """Add a value to Accounts database for specific Account Id."""
        now = datetime.datetime.now()
        cursor = self.sqlite_connection.cursor()
        cursor.execute(
            """
            INSERT INTO Accounts VALUES
                (
                    NULL,
                    "Test User",
                    "test@email.com",
                    1234,
                    4321,
                    123,
                    ?,
                    ?,
                    ""
                )
            """,
            (now, now)
        )
        self.sqlite_connection.commit()

    def get_table(self):
        cursor = self.sqlite_connection.cursor()
        result = cursor.execute("SELECT * FROM Accounts")
        print(result.fetchall())
