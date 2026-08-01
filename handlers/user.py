from telegram import Update
from telegram.ext import ContextTypes

from keyboards.user import main_keyboard
from core.messages import get_message
from core.stickers import get_sticker
from database.db import add_user


async def user_start(update: Update, context: ContextTypes.DEFAULT_TYPE):

    user = update.effective_user

    await add_user(
        user.id,
        user.username,
        user.full_name
    )


    sticker = await get_sticker("start")

    if sticker:
        await context.bot.send_sticker(
            chat_id=user.id,
            sticker=sticker
        )


    text = await get_message(
        "welcome",
        """
سلام رفیق 😎👋

🎟 به بات تیکت امن kingk-configs خوش اومدی 🫴😑

💨 اینجا میتونی خیلی امن و راحت تیکت ثبت کنی و ادمین از داخل همینجا بهت پاسخ بده 🤌🗿

🫷🫪 ولی اگر برای خرید کانفیگ یا دریافت کانفیگ رایگان اومدی، لطفاً مستقیم به پشتیبانی پیام بده:

@mr1kk1rn0 🚀
"""
    )


    await update.message.reply_text(
        text,
        reply_markup=await main_keyboard()
    )
