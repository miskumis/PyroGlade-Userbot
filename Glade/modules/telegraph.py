#
# Copyright (C) 2021-2022 by miskumis@Github, <https://github.com/miskumis >.
#
# This file is part of < https://github.com/miskumis/PyroGlade-Userbot > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/miskumis/PyroGlade-Userbot/blob/main/LICENSE >
#
# All rights reserved.


from pyrogram import Client, filters
from pyrogram.types import Message
from telegraph import Telegraph, exceptions, upload_file

from config import CMD_HANDLER as cmd
from Glade.helpers.basic import edit_or_reply, get_text
from Glade.helpers.tools import *

from .help import *

telegraph = Telegraph()
r = telegraph.create_account(short_name="PyroGlade-Userbot")
auth_url = r["auth_url"]


@Client.on_message(filters.command(["tg", "telegraph"], cmd) & filters.me)
async def uptotelegraph(client: Client, message: Message):
    Glade = await edit_or_reply(message, "`Processing . . .`")
    if not message.reply_to_message:
        await Glade.edit(
            "**Mohon Balas Ke Pesan, Untuk Mendapatkan Link dari Telegraph.**"
        )
        return
    if message.reply_to_message.media:
        if message.reply_to_message.sticker:
            m_d = await convert_to_image(message, client)
        else:
            m_d = await message.reply_to_message.download()
        try:
            media_url = upload_file(m_d)
        except exceptions.TelegraphException as exc:
            await Glade.edit(f"**ERROR:** `{exc}`")
            os.remove(m_d)
            return
        U_done = (
            f"**Berhasil diupload ke** [Telegraph](https://telegra.ph/{media_url[0]})"
        )
        await Glade.edit(U_done)
        os.remove(m_d)
    elif message.reply_to_message.text:
        page_title = get_text(message) if get_text(message) else client.me.first_name
        page_text = message.reply_to_message.text
        page_text = page_text.replace("\n", "<br>")
        try:
            response = telegraph.create_page(page_title, html_content=page_text)
        except exceptions.TelegraphException as exc:
            await Glade.edit(f"**ERROR:** `{exc}`")
            return
        wow_graph = f"**Berhasil diupload ke** [Telegraph](https://telegra.ph/{response['path']})"
        await Glade.edit(wow_graph)


add_command_help(
    "telegraph",
    [
        [
            f"telegraph atau {cmd}tg",
            "Balas ke Pesan Teks atau Media untuk mengunggahnya ke telegraph.",
        ],
    ],
)
