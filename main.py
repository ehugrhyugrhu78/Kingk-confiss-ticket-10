import asyncio
import logging

from telegram.ext import (
    Application,
    CommandHandler,
    CallbackQueryHandler,
    MessageHandler,
    ConversationHandler,
    filters
)

from config import BOT_TOKEN

from database.db import init_db

from handlers.user import user_start
from handlers.ticket import (
    create_ticket_start,
    receive_title,
    receive_message
)

from handlers.admin_dashboard import dashboard

from handlers.settings_manager import (
    settings_menu,
    bot_on,
    bot_off
)

from handlers.admin_reply import save_reply

from states.states import TicketState

from utils.error_handler import error_handler


logging.basicConfig(
    level=logging.INFO
)



async def start():

    await init_db()


    app = Application.builder().token(
        BOT_TOKEN
    ).build()


    ticket_flow = ConversationHandler(

        entry_points=[
            CallbackQueryHandler(
                create_ticket_start,
                pattern="^create_ticket$"
            )
        ],

        states={

            TicketState.TITLE:[
                MessageHandler(
                    filters.TEXT,
                    receive_title
                )
            ],


            TicketState.MESSAGE:[
                MessageHandler(
                    filters.TEXT,
                    receive_message
                )
            ]

        },

        fallbacks=[]

    )


    app.add_handler(
        CommandHandler(
            "start",
            user_start
        )
    )


    app.add_handler(
        CommandHandler(
            "admin",
            dashboard
        )
    )


    app.add_handler(
        ticket_flow
    )


    app.add_handler(
        CallbackQueryHandler(
            settings_menu,
            pattern="^settings$"
        )
    )


    app.add_handler(
        CallbackQueryHandler(
            bot_on,
            pattern="^bot_on$"
        )
    )


    app.add_handler(
        CallbackQueryHandler(
            bot_off,
            pattern="^bot_off$"
        )
    )


    app.add_error_handler(
        error_handler
    )


    await app.run_polling()



if __name__ == "__main__":

    asyncio.run(start())
