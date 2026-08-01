from telegram import Update
from telegram.ext import ContextTypes

from core.settings import set_setting, get_setting
from keyboards.settings import settings_keyboard


async def settings_menu(update: Update, context: ContextTypes.DEFAULT_TYPE):

    query = update.callback_query
    await query.answer()

    status = await get_setting("status")

    text = (
        "⚙️ تنظیمات ربات\n\n"
        f"وضعیت فعلی: {'🟢 فعال' if status != 'off' else '🔴 خاموش'}"
    )

    await query.edit_message_text(
        text,
        reply_markup=settings_keyboard()
    )



async def bot_on(update: Update, context: ContextTypes.DEFAULT_TYPE):

    query = update.callback_query
    await query.answer()

    await set_setting(
        "status",
        "on"
    )

    await query.edit_message_text(
        "🟢 ربات فعال شد"
    )



async def bot_off(update: Update, context: ContextTypes.DEFAULT_TYPE):

    query = update.callback_query
    await query.answer()

    await set_setting(
        "status",
        "off"
    )

    await query.edit_message_text(
        "🔴 ربات خاموش شد"
    )
