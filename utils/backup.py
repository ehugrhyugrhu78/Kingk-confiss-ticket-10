import shutil
import os



def backup_database():

    os.makedirs(
        "backup",
        exist_ok=True
    )


    if os.path.exists(
        "data/kingk_ticket.db"
    ):

        shutil.copy(
            "data/kingk_ticket.db",
            "backup/database_backup.db"
        )
