import os
from .constantes import Constantes
from peewee import *

folderApp = f"{os.path.expanduser('~')}/{Constantes.FOLDER_ROOT}"

metricaDB = SqliteDatabase(f"{folderApp}/{Constantes.DATABASE_NAME}")

# db_models = []