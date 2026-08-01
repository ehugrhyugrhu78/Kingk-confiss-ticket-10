from telegram import InlineKeyboardButton,InlineKeyboardMarkup



def settings_keyboard():

    return InlineKeyboardMarkup([

        [
            InlineKeyboardButton(
                "🟢 ON",
                callback_data="bot_on"
            ),
            InlineKeyboardButton(
                "🔴 OFF",
                callback_data="bot_off"
            )
        ],

        [
            InlineKeyboardButton(
                "🎭 مدیریت استیکر",
                callback_data="stickers"
            )
        ],

        [
            InlineKeyboardButton(
                "📝 مدیریت پیام",
                callback_data="messages"
            )
        ]

    ])
