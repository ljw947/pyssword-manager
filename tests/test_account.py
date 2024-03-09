"""Test cases for accounts database."""

from pathlib import Path

from pyssword_lib.account import Accounts

def test_default_accounts_database_values(tmp_path):
    """Test that accounts database is initialised with expected values."""
    account_database = Accounts(tmp_path)
    assert account_database.database_dir is tmp_path
    assert account_database.database_name == "accounts"
    assert account_database.database_file_path == Path(tmp_path / "accounts.db")
    assert account_database.sqlite_connection is not None


def test_accounts_database_instantiation(tmp_path):
    """Test that accounts database file is created on disk."""
    account_database = Accounts(tmp_path)  # pylint: disable=unused-variable
    assert Path(tmp_path / "accounts.db").exists()


def test_add_table(tmp_path):
    """Test that the default table can be added to accounts database."""
    account_database = Accounts(tmp_path)
    account_database.add_table()
    cursor = account_database.sqlite_connection.cursor()
    result = cursor.execute("SELECT name FROM sqlite_master WHERE name='Accounts'")
    assert result.fetchone() is not None
