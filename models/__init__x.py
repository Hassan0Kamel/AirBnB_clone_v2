#!/usr/bin/python3
""" Determied object.
"""
from os import getenv


if getenv('HBNB_TYPE_STORAGE') == 'db':
    from.engine.db_storage import DBStorage
    storage = DBStorage()
    storage.reload()

else:
    from .engine.file_storage import FileStorage
    storage = FileStorage()
    storage.reload()
