import aiosqlite
import datetime
import logging

DB_NAME = "bot.db"

logger = logging.getLogger(__name__)


async def init_db():
    async with aiosqlite.connect(DB_NAME) as db:

        await db.execute("""
        CREATE TABLE IF NOT EXISTS tickets(
            ticket_id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER,
            title TEXT,
            status TEXT DEFAULT 'open',
            created_at TEXT
        )
        """)

        await db.execute("""
        CREATE TABLE IF NOT EXISTS messages(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            ticket_id INTEGER,
            sender_id INTEGER,
            message_type TEXT,
            file_id TEXT,
            caption TEXT,
            created_at TEXT
        )
        """)

        await db.commit()



async def add_message(
    ticket_id,
    sender_id,
    message_type="text",
    file_id=None,
    caption=""
):

    async with aiosqlite.connect(DB_NAME) as db:

        await db.execute(
            """
            INSERT INTO messages
            (
                ticket_id,
                sender_id,
                message_type,
                file_id,
                caption,
                created_at
            )
            VALUES (?, ?, ?, ?, ?, ?)
            """,
            (
                ticket_id,
                sender_id,
                message_type,
                file_id,
                caption,
                datetime.datetime.now().strftime(
                    "%Y-%m-%d %H:%M:%S"
                )
            )
        )

        await db.commit()



async def create_ticket(user_id, title):

    async with aiosqlite.connect(DB_NAME) as db:

        cursor = await db.execute(
            """
            INSERT INTO tickets
            (
                user_id,
                title,
                created_at
            )
            VALUES (?, ?, ?)
            """,
            (
                user_id,
                title,
                datetime.datetime.now().strftime(
                    "%Y-%m-%d %H:%M:%S"
                )
            )
        )

        await db.commit()

        return cursor.lastrowid



async def get_ticket(ticket_id):

    async with aiosqlite.connect(DB_NAME) as db:

        cursor = await db.execute(
            """
            SELECT * FROM tickets
            WHERE ticket_id=?
            """,
            (ticket_id,)
        )

        return await cursor.fetchone()



async def change_status(ticket_id, status):

    async with aiosqlite.connect(DB_NAME) as db:

        await db.execute(
            """
            UPDATE tickets
            SET status=?
            WHERE ticket_id=?
            """,
            (
                status,
                ticket_id
            )
        )

        await db.commit()
