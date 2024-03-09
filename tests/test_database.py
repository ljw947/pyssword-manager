"""Test cases for Database class."""

from pathlib import Path

from pyssword_lib.database import Database


def test_default_database_values(tmp_path):
    """Test that an empty database is initialised with the expected values."""
    test_database = Database(tmp_path)
    assert test_database.database_dir is tmp_path
    assert test_database.database_name is None
    assert test_database.database_file_path is None
    assert test_database.sqlite_connection is None


def test_database_instantiation(tmp_path):
    """Test that a database file is created on disk."""
    test_database = Database(tmp_path)
    test_database.initialise_database_file()
    assert Path(tmp_path / "None.db").exists()


def test_database_connection(tmp_path):
    """Test that the database is connectable"""
    test_database = Database(tmp_path)
    test_database.initialise_database_file()
    assert test_database.sqlite_connection is not None


def test_database_works(tmp_path):
    """Test that the database file is usable"""
    test_database = Database(tmp_path)
    test_database.initialise_database_file()
    assert test_database.sqlite_connection is not None
    cursor = test_database.sqlite_connection.cursor()
    cursor.execute("CREATE TABLE test_table(test_col)")
    result = cursor.execute("SELECT * FROM test_table").fetchall()
    assert result == []
