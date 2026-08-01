import shutil
import datetime



def create_backup():

    name = (
        "backup_"
        +
        datetime.datetime.now()
        .strftime("%Y%m%d")
        +
        ".db"
    )


    shutil.copy(
        "bot.db",
        name
    )
