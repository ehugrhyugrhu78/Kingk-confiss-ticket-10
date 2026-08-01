from telegram import InlineKeyboardButton, InlineKeyboardMarkup



def confirm_keyboard():

    return InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    "✅ ارسال",
                    callback_data="send_ticket"
                )
            ],
            [
                InlineKeyboardButton(
                    "❌ لغو",
                    callback_data="cancel_ticket"
                )
            ]
        ]
    )
