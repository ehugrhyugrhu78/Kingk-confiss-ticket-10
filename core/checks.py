from core.settings import get_setting



async def bot_enabled():

    status = await get_setting(
        "status"
    )


    return status != "off"
