from os import getenv

from pyrogram import filters
from dotenv import load_dotenv

load_dotenv()

API_ID = "25742938"
# -------------------------------------------------------------
API_HASH = "b35b715fe8dc0a58e8048988286fc5b6"
# --------------------------------------------------------------
BOT_TOKEN = getenv("BOT_TOKEN", "7694603106:AAHalbxgqIVkY3jPlGrLBljKoxfAGOndo7A")
STRING1 = getenv("STRING_SESSION", "BQC86fAAff9lE8MLuow-iVQYtdvKUudi2y7cF-em1T0ip_FSXyKkaiaSoYWcN_-e5ytovWXcvyt1sCqWqL7SocByc2RHHdS7fDc6j5qAK62Sm3TD7NDlRU9rdGVP8nY0nLyMcvrAY2d-Plhby8222k6adTSK9j6epXPma2V6AivEChdzPtWrp-7S8aPUbmyJwsUHlj19CcOVoAdF0TMXnGEGGJ85gV0HYCBAflnwKHn7NOliFkHnF_rx3vEEpqQOLURvFeWfb8LEISHhLMzO5-a_CKrRn3QHUZpoo-ZqeCkAgQ2MZJmVsO49EGMjpj4ITOKUWzF1ES8tNbY3MYSDb0S1tSBTGwAAAAHV1eN-AA")
DB_NAME = "shizuDB"
MONGO_URL = getenv("MONGO_URL", "mongodb+srv://architect2002:architect2002@cluster0.ccinu.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
OWNER_ID = int(getenv("OWNER_ID", "7882531710"))
BOT_ID = int(getenv("BOT_ID", "7694603106"))
SUPPORT_GRP = "PBX_CHAT"
UPDATE_CHNL = "HEROKUBIN_01"
OWNER_USERNAME = "Itz_me_Makkaru"
TIME_ZONE = "Asia/Kolkata"
LOG_GROUP_ID = int(getenv("LOG_GROUP_ID", "-1002472747523"))
# --------------------------------------------------------------
SUDOERS = list(map(int, getenv("SUDOERS", "7882531710").split()))
# --------------------------------------------------------------

### DONT TOUCH or EDIT codes after this line
BANNED_USERS = filters.user()

# For customized or modified Repository
UPSTREAM_REPO = getenv(
    "UPSTREAM_REPO",
    "https://github.com/Badhacker98/ShizuChat_Bot",
)
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "main")
