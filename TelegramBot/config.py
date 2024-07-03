import json
from os import getenv
from dotenv import load_dotenv

load_dotenv("config.env")

API_ID = int(getenv("20841292"))
API_HASH = getenv("58c4e84b9b2506684df6447d3e324dd9")
BOT_TOKEN = getenv("7451705797:AAEu-w-v4M-hyrYzM_tUCER4ueW_ZAdm520")

SUDO_USERID = json.loads(getenv("6052303737"))
AUTHORIZED_CHATS = json.loads(getenv("0"))
