from enum import IntEnum


class TicketState(IntEnum):

    TITLE = 1
    MESSAGE = 2
    CONFIRM = 3
    ADMIN_REPLY = 4
    EDIT_MESSAGE = 5
