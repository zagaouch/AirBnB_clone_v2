""" Check value of hbnb storage trype"""

import os


if os.getenv("HBNG_TYPE_STORAGE") == "db":
    from db_storage import DBStorage
    storage = DBStorage()
else:
    from file_storage import FileStorage
    storage = FileStorage()
storage.reload()
