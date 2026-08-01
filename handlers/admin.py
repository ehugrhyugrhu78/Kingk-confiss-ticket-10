from telegram import Update
from telegram.ext import ContextTypes

from config import ADMIN_ID
from keyboards.admin import admin_keyboard



async def admin_panel(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
):

    user = update.effective_user


    if user.id != ADMIN_ID:
        return


    await update.message.reply_text(
        """
👑 پنل مدیریت KingK

تمام امکانات ربات از اینجا کنترل می‌شود 🚀
""",
        reply_markup=admin_keyboard()
    )
