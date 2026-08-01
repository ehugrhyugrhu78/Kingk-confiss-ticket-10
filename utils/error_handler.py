import logging


logger = logging.getLogger(
    "kingk-ticket"
)



async def error_handler(
    update,
    context
):

    logger.error(
        f"ERROR: {context.error}"
    )


    try:

        if update and update.effective_message:

            await update.effective_message.reply_text(
                "❌ یک خطای موقت رخ داد، دوباره تلاش کنید."
            )

    except:

        pass
