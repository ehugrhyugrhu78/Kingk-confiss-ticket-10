from telegram import Update
from telegram.ext import ContextTypes

from database.admin import get_admin_tickets, ticket_count
from keyboards.pagination import pagination_keyboard



async def admin_ticket_pages(
    update:Update,
    context:ContextTypes.DEFAULT_TYPE
):

    query = update.callback_query

    await query.answer()


    page = int(
        query.data.split("_")[-1]
    )


    limit = 5
    offset = (
        page - 1
    ) * limit


    tickets = await get_admin_tickets(
        limit=limit,
        offset=offset
    )


    total = await ticket_count()

    pages = max(
        1,
        (total + limit - 1)//limit
    )


    text = "🎟 لیست تیکت‌ها:\n\n"


    for t in tickets:

        text += (
            f"🎫 #{t[0]}\n"
            f"👤 کاربر: {t[1]}\n"
            f"📌 {t[2]}\n"
            f"━━━━━━━━━━\n"
        )


    await query.edit_message_text(
        text,
        reply_markup=pagination_keyboard(
            page,
            pages,
            "tickets"
        )
    )
