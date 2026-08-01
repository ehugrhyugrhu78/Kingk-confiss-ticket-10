from telegram import InlineKeyboardButton, InlineKeyboardMarkup



def admin_ticket_menu():

    return InlineKeyboardMarkup([

        [
            InlineKeyboardButton(
                "📂 همه تیکت‌ها",
                callback_data="all_tickets"
            )
        ],

        [
            InlineKeyboardButton(
                "🟢 تیکت‌های باز",
                callback_data="open_tickets"
            )
        ],

        [
            InlineKeyboardButton(
                "🔴 تیکت‌های بسته",
                callback_data="closed_tickets"
            )
        ],

        [
            InlineKeyboardButton(
                "⬅️ برگشت",
                callback_data="admin_back"
            )
        ]

    ])
