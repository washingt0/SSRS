from src.config import *
from os import path, makedirs

if not path.exists(CONFIG_FOLDER):
    makedirs(CONFIG_FOLDER, exist_ok=True)

if not path.exists(INDEX_ROOT):
    makedirs(CONFIG_FOLDER, exist_ok=True)
