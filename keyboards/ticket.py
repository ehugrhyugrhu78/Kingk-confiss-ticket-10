from telegram import InlineKeyboardButton, InlineKeyboardMarkup


def ticket_menu():

    return InlineKeyboardMarkup([
        [
            InlineKeyboardButton(
                "🟢 ساخت تیکت جدید 🎟",
                callback_data="create_ticket"
            )
        ],
        [
            InlineKeyboardButton(
                "📂 تیکت‌های من",
                callback_data="my_tickets"
            )
        ]
    ])



def ticket_confirm():

    return InlineKeyboardMarkup([
        [
            InlineKeyboardButton(
                "✅ ارسال تیکت",
                callback_data="confirm_ticket"
            )
        ],
        [
            InlineKeyboardButton(
                "✏️ ویرایش",
                callback_data="edit_ticket"
            )
        ],
        [
            InlineKeyboardButton(
                "❌ لغو",
                callback_data="cancel_ticket"
            )
        ]
    ])
