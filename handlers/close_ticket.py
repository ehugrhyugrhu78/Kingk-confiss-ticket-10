from database.tickets import change_status



async def close_ticket(
    update,
    context
):

    query = update.callback_query


    ticket_id = int(
        query.data.split("_")[-1]
    )


    await change_status(
        ticket_id,
        "closed"
    )


    await query.answer(
        "تیکت بسته شد 🔒"
    )
