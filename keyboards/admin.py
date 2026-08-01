from telegram import InlineKeyboardButton, InlineKeyboardMarkup


def admin_keyboard():

    return InlineKeyboardMarkup([
        [
            InlineKeyboardButton(
                "🎟 مدیریت تیکت‌ها",
                callback_data="admin_tickets"
            )
        ],
        [
            InlineKeyboardButton(
                "⚙️ تنظیمات",
                callback_data="settings"
            )
        ],
        [
            InlineKeyboardButton(
                "🎨 ویرایش ربات",
                callback_data="editor"
            )
        ]
    ])
