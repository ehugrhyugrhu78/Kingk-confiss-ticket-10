from core.checks import bot_enabled



async def check_status(
    update,
    context
):

    if not await bot_enabled():

        await update.effective_message.reply_text(
            """
✨️ درحال‌حاضر ربات غیرفعال میباشد!

بعدا تلاش کنید یا مستقیم به پشتیبانی بگویید 🎁

@mr1kk1rn0
"""
        )

        return False


    return True
