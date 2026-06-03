from dataclasses import dataclass
import sqlite3
from pathlib import Path


@dataclass(frozen=True)
class StoredMessage:
    user_id: int
    username: str | None
    text: str
    category: str
    urgency: str
    needs_human: bool


class SupportStorage:
    def __init__(self, database_path: str):
        self.database_path = database_path

    def connect(self) -> sqlite3.Connection:
        Path(self.database_path).parent.mkdir(parents=True, exist_ok=True)
        connection = sqlite3.connect(self.database_path)
        connection.row_factory = sqlite3.Row
        return connection

    def migrate(self) -> None:
        with self.connect() as connection:
            connection.execute(
                """
                CREATE TABLE IF NOT EXISTS messages (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    user_id INTEGER NOT NULL,
                    username TEXT,
                    text TEXT NOT NULL,
                    category TEXT NOT NULL,
                    urgency TEXT NOT NULL,
                    needs_human INTEGER NOT NULL,
                    created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP
                )
                """
            )

    def save_message(self, message: StoredMessage) -> int:
        with self.connect() as connection:
            cursor = connection.execute(
                """
                INSERT INTO messages (
                    user_id, username, text, category, urgency, needs_human
                )
                VALUES (?, ?, ?, ?, ?, ?)
                """,
                (
                    message.user_id,
                    message.username,
                    message.text,
                    message.category,
                    message.urgency,
                    int(message.needs_human),
                ),
            )
            return int(cursor.lastrowid)

    def list_recent_messages(self, limit: int = 20) -> list[sqlite3.Row]:
        with self.connect() as connection:
            return list(
                connection.execute(
                    "SELECT * FROM messages ORDER BY id DESC LIMIT ?",
                    (limit,),
                )
            )