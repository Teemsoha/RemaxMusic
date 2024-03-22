#
# Copyright (C) 2021-present by TeamRemax@Github, < https://github.com/TeamRemax >.
#
# This file is part of < https://github.com/TeamRemax/RemaxBotBot > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/TeamRemax/RemaxBotBot/blob/master/LICENSE >
#
# All rights reserved.
#

from pyrogram import filters

import config
from remaxes import get_command
from RemaxBot import app
from RemaxBot.misc import SUDOERS
from RemaxBot.utils.database import add_off, add_on
from RemaxBot.utils.decorators.language import language

# Commands
LOGGER_COMMAND = get_command("LOGGER_COMMAND")


@app.on_message(filters.command(["السجل"],"") & SUDOERS)
@language
async def logger(client, message, _):
    usage = _["log_1"]
    if len(message.command) != 2:
        return await message.reply_text(usage)
    state = message.text.split(None, 1)[1].strip()
    state = state.lower()
    if state == "تفعيل":
        await add_on(config.LOG)
        await message.reply_text(_["log_2"])
    elif state == "تعطيل":
        await add_off(config.LOG)
        await message.reply_text(_["log_3"])
    else:
        await message.reply_text(usage)
