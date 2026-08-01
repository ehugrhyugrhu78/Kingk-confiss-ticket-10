from telegram import InlineKeyboardButton, InlineKeyboardMarkup

from core.builder import get_buttons



async def main_keyboard():

    buttons = await get_buttons()

    keyboard = []


    for text, action in buttons:

        keyboard.append(
            [
                InlineKeyboardButton(
                    text,
                    callback_data=action
                )
            ]
        )


    return InlineKeyboardMarkup(
        keyboard
    )
