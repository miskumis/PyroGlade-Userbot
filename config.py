#
# Copyright (C) 2021-2022 by miskumis@Github, <https://github.com/miskumis >.
#
# This file is part of < https://github.com/miskumis/PyroGlade-Userbot > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/miskumis/PyroGlade-Userbot/blob/main/LICENSE >
#
# All rights reserved.

from base64 import b64decode
from os import getenv

from dotenv import load_dotenv

load_dotenv("config.env")


API_HASH = getenv("API_HASH")
API_ID = int(getenv("API_ID", ""))
BLACKLIST_CHAT = getenv("BLACKLIST_CHAT", None)
if not BLACKLIST_CHAT:
    BLACKLIST_CHAT = [-1001579296330]
BLACKLIST_GCAST = {int(x) for x in getenv("BLACKLIST_GCAST", "").split()}
BOTLOG_CHATID = int(getenv("BOTLOG_CHATID") or 0)
BOT_VER = ".0.1"
BRANCH = "main"
CHANNEL = getenv("CHANNEL", "GladeSupportChannel")
CMD_HANDLER = getenv("CMD_HANDLER", ".")
DB_URL = getenv("DATABASE_URL", "")
GIT_TOKEN = getenv(
    "GIT_TOKEN",
    b64decode("Z2hwXzBpakdCZXNSQWdqY3haUDRHVVZhQ3VWWjA4cEMxaTNzUEtxVQ==").decode(
        "utf-8"
    ),
)
GROUP = getenv("GROUP", "GladeSupportGroup")
HEROKU_API_KEY = getenv("HEROKU_API_KEY", None)
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME", None)
PMPERMIT_PIC = getenv("PMPERMIT_PIC", None)
REPO_URL = getenv(
    "REPO_URL",
    b64decode("aHR0cHM6Ly9naXRodWIuY29tL21pc2t1bWlzL1B5cm9HbGFkZS1Vc2VyYm90").decode("utf-8"),
)
STRING_SESSION1 = getenv("STRING_SESSION1", "")
STRING_SESSION2 = getenv("STRING_SESSION2", "")
STRING_SESSION3 = getenv("STRING_SESSION3", "")
STRING_SESSION4 = getenv("STRING_SESSION4", "")
STRING_SESSION5 = getenv("STRING_SESSION5", "")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "").split()))
