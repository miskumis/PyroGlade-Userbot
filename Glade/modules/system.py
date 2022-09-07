#
# Copyright (C) 2021-2022 by miskumis@Github, <https://github.com/miskumis >.
#
# This file is part of < https://github.com/miskumis/PyroGlade-Userbot > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/miskumis/PyroGlade-Userbot/blob/master/LICENSE >
#
# All rights reserved.

import sys
from os import environ, execle, remove

from pyrogram import Client, filters
from pyrogram.types import Message

from config import CMD_HANDLER as cmd
from Glade import BOTLOG_CHATID, LOGGER
from Glade.helpers.basic import edit_or_reply
from Glade.helpers.misc import HAPP

from .help import add_command_help


@Client.on_message(filters.command("restart", cmd) & filters.me)
async def restart_bot(_, message: Message):
    try:
        msg = await edit_or_reply(message, "`Restarting bot...`")
        LOGGER(__name__).info("BOT SERVER RESTARTED !!")
    except BaseException as err:
        LOGGER(__name__).info(f"{err}")
        return
    await msg.edit_text("✅ Bot has restarted !\n\n")
    if HAPP is not None:
        HAPP.restart()
    else:
        args = [sys.executable, "-m", "Glade"]
        execle(sys.executable, *args, environ)


@Client.on_message(filters.command("shutdown", cmd) & filters.me)
async def shutdown_bot(client: Client, message: Message):
    if BOTLOG_CHATID:
        await client.send_message(
            BOTLOG_CHATID,
            "**#SHUTDOWN** \n"
            "**PyroGlade-Userbot** telah di matikan!\nJika ingin menghidupkan kembali silahkan buka heroku",
        )
    await edit_or_reply(message, "**PyroMan-Userbot Berhasil di matikan!**")
    if HAPP is not None:
        HAPP.process_formation()["worker"].scale(0)
    else:
        sys.exit(0)


@Client.on_message(filters.command("logs", cmd) & filters.me)
async def logs_ubot(client: Client, message: Message):
    if HAPP is None:
        return await edit_or_reply(
            message,
            "Pastikan `HEROKU_API_KEY` dan `HEROKU_APP_NAME` anda dikonfigurasi dengan benar di config vars heroku",
        )
    Glade = await edit_or_reply(message, "**Sedang Mengambil Logs Heroku**")
    with open("Logs-Heroku.txt", "w") as log:
        log.write(HAPP.get_log())
    await client.send_document(
        message.chat.id,
        "Logs-Heroku.txt",
        thumb="Glade/resources/logo.jpg",
        caption="**Ini Logs Heroku anda**",
    )
    await Glade.delete()
    remove("Logs-Heroku.txt")


add_command_help(
    "system",
    [
        ["restart", "Untuk merestart userbot."],
        ["shutdown", "Untuk mematikan userbot."],
        ["logs", "Untuk melihat logs userbot."],
    ],
)
