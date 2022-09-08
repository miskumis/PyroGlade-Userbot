#
# Copyright (C) 2021-2022 by miskumis@Github, <https://github.com/miskumis >.
#
# This file is part of < https://github.com/miskumis/PyroGlade-Userbot > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/miskumis/PyroGlade-Userbot/blob/main/LICENSE >
#
# All rights reserved.

import aiohttp


async def expand_url(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(f"http://expandurl.com/api/v1/?url={url}") as resp:
            expanded = await resp.text()

        return expanded if expanded != "false" and expanded[:-1] != url else None
