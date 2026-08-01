from telegram import Update
from telegram.ext import ContextTypes

from keyboards.admin import admin_keyboard



async def dashboard(
    update:Update,
    context:ContextTypes.DEFAULT_TYPE
):

    await update.message.reply_text(
        "👑 پنل مدیریت",
        reply_markup=admin_keyboard()
    )
