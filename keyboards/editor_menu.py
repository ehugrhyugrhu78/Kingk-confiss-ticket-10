from telegram import InlineKeyboardButton, InlineKeyboardMarkup


def editor_menu():

    return InlineKeyboardMarkup([

        [
            InlineKeyboardButton(
                "📝 تغییر پیام",
                callback_data="edit_message"
            )
        ],

        [
            InlineKeyboardButton(
                "🎭 تغییر استیکر",
                callback_data="edit_sticker"
            )
        ],

        [
            InlineKeyboardButton(
                "🔘 تغییر دکمه‌ها",
                callback_data="edit_buttons"
            )
        ]

    ])
