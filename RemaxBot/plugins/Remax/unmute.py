#
# Copyright (C) 2021-present by TeamRemax@Github, < https://github.com/TeamRemax >.
#
# This file is part of < https://github.com/TeamRemax/RemaxBotBot > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/TeamRemax/RemaxBotBot/blob/master/LICENSE >
#
# All rights reserved.
#s

from pyrogram import filters
from pyrogram.types import Message

from config import BANNED_USERS
from remaxes import get_command
from RemaxBot import app
from RemaxBot.core.call import Remax
from RemaxBot.utils.database import is_muted, mute_off
from RemaxBot.utils.decorators import AdminRightsCheck

# Commands
UNMUTE_COMMAND = get_command("UNMUTE_COMMAND")


@app.on_message(
    filters.command(UNMUTE_COMMAND)
    & filters.group
    & ~BANNED_USERS
)
@AdminRightsCheck
async def unmute_admin(Client, message: Message, _, chat_id):
    if not len(message.command) == 1 or message.reply_to_message:
        return await message.reply_text(_["general_2"])
    if not await is_muted(chat_id):
        return await message.reply_text(_["admin_7"])
    await mute_off(chat_id)
    await Remax.unmute_stream(chat_id)
    await message.reply_text(
        _["admin_8"].format(message.from_user.mention)
    )
