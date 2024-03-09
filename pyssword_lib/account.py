"""Account database"""

import datetime

from pyssword_lib.database import Database


class Accounts(Database):
    """Accounts class, handles user accounts"""
    def __init__(self):
        Database.__init__(self)
        self.database_name = "accounts"
        self.initialise_database_file()

    def add_table(self):
        """Sets up accounts table with relevant columns."""
        cursor = self.sqlite_connection.cursor()
        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS user
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
        now = datetime.datetime.now()
        cursor = self.sqlite_connection.cursor()
        cursor.execute(
            """
            INSERT INTO user VALUES
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
        result = cursor.execute("SELECT * FROM USER")
        print(result.fetchall())
