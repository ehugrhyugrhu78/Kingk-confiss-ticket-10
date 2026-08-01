import asyncio
import logging

from telegram.ext import (
    Application,
    CommandHandler
)

from config import BOT_TOKEN
from utils.logger import logger


# =========================
# Start Message
# =========================

async def start(update, context):

    text = """
سلام رفیق 😎👋

🎟 به بات تیکت امن kingk-configs خوش اومدی 🫴😑

💨 اینجا میتونی خیلی امن و راحت تیکت ثبت کنی و ادمین از داخل همینجا بهت پاسخ بده 🤌🗿

🫷🫪 ولی اگر برای خرید کانفیگ یا دریافت کانفیگ رایگان اومدی، لطفاً مستقیم به پشتیبانی پیام بده:

@mr1kk1rn0 🚀
"""

    await update.message.reply_text(text)


# =========================
# Error Handler
# =========================

async def error_handler(update, context):

    logger.error(
        f"ERROR: {context.error}"
    )

    try:
        if update and update.effective_message:
            await update.effective_message.reply_text(
                "❌ یک خطای موقت رخ داد.\nلطفاً دوباره تلاش کنید 🙏"
            )

    except Exception:
        pass



# =========================
# Main
# =========================

async def main():

    logger.info(
        "🚀 Starting KingK Ticket Bot..."
    )

    app = (
        Application
        .builder()
        .token(BOT_TOKEN)
        .build()
    )


    # Commands
    app.add_handler(
        CommandHandler(
            "start",
            start
        )
    )


    # Errors
    app.add_error_handler(
        error_handler
    )


    logger.info(
        "✅ Bot is running..."
    )


    await app.initialize()
    await app.start()
    await app.updater.start_polling()


    # Keep alive
    await asyncio.Event().wait()



if __name__ == "__main__":

    try:
        asyncio.run(main())

    except KeyboardInterrupt:
        logging.info(
            "Bot stopped"
        )

    except Exception as e:
        logging.error(
            f"Fatal error: {e}"
        )import asyncio
import logging

from telegram.ext import (
    Application,
    CommandHandler
)

from config import BOT_TOKEN
from utils.logger import logger


# =========================
# Start Message
# =========================

async def start(update, context):

    text = """
سلام رفیق 😎👋

🎟 به بات تیکت امن kingk-configs خوش اومدی 🫴😑

💨 اینجا میتونی خیلی امن و راحت تیکت ثبت کنی و ادمین از داخل همینجا بهت پاسخ بده 🤌🗿

🫷🫪 ولی اگر برای خرید کانفیگ یا دریافت کانفیگ رایگان اومدی، لطفاً مستقیم به پشتیبانی پیام بده:

@mr1kk1rn0 🚀
"""

    await update.message.reply_text(text)


# =========================
# Error Handler
# =========================

async def error_handler(update, context):

    logger.error(
        f"ERROR: {context.error}"
    )

    try:
        if update and update.effective_message:
            await update.effective_message.reply_text(
                "❌ یک خطای موقت رخ داد.\nلطفاً دوباره تلاش کنید 🙏"
            )

    except Exception:
        pass



# =========================
# Main
# =========================

async def main():

    logger.info(
        "🚀 Starting KingK Ticket Bot..."
    )

    app = (
        Application
        .builder()
        .token(BOT_TOKEN)
        .build()
    )


    # Commands
    app.add_handler(
        CommandHandler(
            "start",
            start
        )
    )


    # Errors
    app.add_error_handler(
        error_handler
    )


    logger.info(
        "✅ Bot is running..."
    )


    await app.initialize()
    await app.start()
    await app.updater.start_polling()


    # Keep alive
    await asyncio.Event().wait()



if __name__ == "__main__":

    try:
        asyncio.run(main())

    except KeyboardInterrupt:
        logging.info(
            "Bot stopped"
        )

    except Exception as e:
        logging.error(
            f"Fatal error: {e}"
        )
