from telegram import InlineKeyboardButton, InlineKeyboardMarkup


def pagination_keyboard(page, total_pages, prefix):

    buttons = []


    row = []

    if page > 1:
        row.append(
            InlineKeyboardButton(
                "⬅️ قبلی",
                callback_data=f"{prefix}_{page-1}"
            )
        )


    row.append(
        InlineKeyboardButton(
            f"📄 {page}/{total_pages}",
            callback_data="none"
        )
    )


    if page < total_pages:
        row.append(
            InlineKeyboardButton(
                "بعدی ➡️",
                callback_data=f"{prefix}_{page+1}"
            )
        )


    buttons.append(row)


    buttons.append(
        [
            InlineKeyboardButton(
                "🔙 برگشت",
                callback_data="admin_back"
            )
        ]
    )


    return InlineKeyboardMarkup(buttons)
