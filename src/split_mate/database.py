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
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS transactions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL,
            amount REAL NOT NULL,
            month INTEGER NOT NULL,
            year INTEGER NOT NULL,
            type_id INTEGER NOT NULL,
            shared_with TEXT,
            is_income BOOL NOT NULL,
            FOREIGN KEY (user_id) REFERENCES users(id),
            FOREIGN KEY (type_id) REFERENCES expenses_type(id)
        )
    """)

    # Create 'debts' table:
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS debts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            debtor_id INTEGER NOT NULL,
            creditor_id INTEGER NOT NULL,
            amount REAL NOT NULL,
            FOREIGN KEY (debtor_id) REFERENCES users(id),
            FOREIGN KEY (creditor_id) REFERENCES users(id)
        )
    """)

    # Insert default expenses types (if not existing already):
    default_expense_types = [
        "groceries",
        "healthcare",
        "taxes",
        "restaurants",
        "shopping",
    ]
    for expense_type in default_expense_types:
        cursor.execute(
            "INSERT OR IGNORE INTO expense_types (type_name) VALUES (?)",
            (expense_type,),
        )

    db.commit()
    db.close()


def clear_all_data() -> None:
    """Deleting the database file and reinitializing it with empty tables."""
    if DB_FILE_PATH.exists():
        os.remove(DB_FILE_PATH)
    init_database()


if __name__ == '__main__':
    print("Initializing database...")
    init_database()
    print("Database initialized successfully.")
