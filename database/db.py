import aiosqlite
import datetime
import os

DB_NAME = "data/kingk_ticket.db"


async def connect_db():
    os.makedirs("data", exist_ok=True)
    return await aiosqlite.connect(DB_NAME)


async def init_db():

    async with await connect_db() as db:

        await db.execute("""
        CREATE TABLE IF NOT EXISTS users(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER UNIQUE,
            username TEXT,
            full_name TEXT,
            created_at TEXT
        )
        """)


        await db.execute("""
        CREATE TABLE IF NOT EXISTS tickets(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER,
            title TEXT,
            status TEXT DEFAULT 'open',
            created_at TEXT
        )
        """)


        await db.execute("""
        CREATE TABLE IF NOT EXISTS ticket_messages(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            ticket_id INTEGER,
            sender_id INTEGER,
            sender_type TEXT,
            message_type TEXT,
            content TEXT,
            file_id TEXT,
            created_at TEXT
        )
        """)


        await db.execute("""
        CREATE TABLE IF NOT EXISTS settings(
            key TEXT PRIMARY KEY,
            value TEXT
        )
        """)


        await db.execute("""
        CREATE TABLE IF NOT EXISTS buttons(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            text TEXT,
            action TEXT,
            position INTEGER DEFAULT 0,
            enabled INTEGER DEFAULT 1
        )
        """)


        await db.execute("""
        CREATE TABLE IF NOT EXISTS messages(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            key TEXT UNIQUE,
            text TEXT
        )
        """)


        await db.execute("""
        CREATE TABLE IF NOT EXISTS stickers(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            file_id TEXT
        )
        """)


        await db.commit()



async def add_user(user_id, username, full_name):

    async with await connect_db() as db:

        await db.execute(
            """
            INSERT OR IGNORE INTO users
            (user_id, username, full_name, created_at)
            VALUES (?, ?, ?, ?)
            """,
            (
                user_id,
                username,
                full_name,
                datetime.datetime.now().isoformat()
            )
        )

        await db.commit()
