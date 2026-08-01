from telegram import InlineKeyboardButton, InlineKeyboardMarkup



def ticket_actions(ticket_id):

    return InlineKeyboardMarkup([

        [
            InlineKeyboardButton(
                "💬 پاسخ",
                callback_data=f"reply_{ticket_id}"
            )
        ],

        [
            InlineKeyboardButton(
                "🔒 بستن",
                callback_data=f"close_{ticket_id}"
            )
        ],

        [
            InlineKeyboardButton(
                "🔓 باز کردن",
                callback_data=f"open_{ticket_id}"
            )
        ]

    ])
