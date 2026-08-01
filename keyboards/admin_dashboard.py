from telegram import InlineKeyboardButton, InlineKeyboardMarkup


def dashboard_keyboard():

    return InlineKeyboardMarkup([

        [
            InlineKeyboardButton(
                "🎟 تیکت‌ها",
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
                "🎨 ظاهر ربات",
                callback_data="editor"
            )
        ]

    ])
