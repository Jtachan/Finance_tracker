"""Module in charge of the operations with the database."""

import os
import pathlib as pl
import sqlite3

# Directory path:
DATA_DIR = pl.Path(os.getenv("LOCALAPPDATA")) / "SplitMate"
DATA_DIR.mkdir(parents=True, exist_ok=True)

# SQLite database file path:
DB_FILE_PATH = DATA_DIR / "finances.db"


def init_database() -> None:
    """SQLite database initialization.
    Creates the database and the tables it contains when this one doesn't exist.
    """
    db = sqlite3.connect(DB_FILE_PATH)
    cursor = db.cursor()

    # Create 'users' table:
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL UNIQUE
        )
    """)

    # Create 'expenses types' table:
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS expense_types(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            type_name TEXT NOT NULL UNIQUE
        )
    """)

    # Create 'transactions' table:
    raise NotImplementedError("This function wasn't finalized")
