from database.tickets import change_status



async def reopen_ticket(
    update,
    context
):

    query = update.callback_query

    ticket_id = int(
        query.data.split("_")[-1]
    )


    await change_status(
        ticket_id,
        "open"
    )


    await query.answer(
        "تیکت دوباره باز شد ✅"
    )
