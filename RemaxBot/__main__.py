#
# Copyright (C) 2021-present by TeamRemax@Github, < https://github.com/TeamRemax >.
#
# This file is part of < https://github.com/TeamRemax/RemaxBotBot > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/TeamRemax/RemaxBotBot/blob/master/LICENSE >
#
# All rights reserved.
#

import asyncio
import importlib
import sys

from pyrogram import idle
from pytgcalls.exceptions import NoActiveGroupCall

import config
from config import BANNED_USERS
from RemaxBot import LOGGER, app, userbot
from RemaxBot.core.call import Remax
from RemaxBot.plugins import ALL_MODULES
from RemaxBot.utils.database import get_banned_users, get_gbanned

loop = asyncio.get_event_loop_policy().get_event_loop()


async def init():
    if (
        not config.STRING1
        and not config.STRING2
        and not config.STRING3
        and not config.STRING4
        and not config.STRING5
    ):
        LOGGER("RemaxBot").error(
            "لم يتم تعريف Vars للعملاء المساعدين!.. جارٍ الخروج من العملية."
        )
        return
    if (
        not config.SPOTIFY_CLIENT_ID
        and not config.SPOTIFY_CLIENT_SECRET
    ):
        LOGGER("RemaxBot").warning(
            "لم يتم تحديد Spotify Vars. لن يتمكن الروبوت الخاص بك من تشغيل استعلامات Spotify."
        )
    try:
        users = await get_gbanned()
        for user_id in users:
            BANNED_USERS.add(user_id)
        users = await get_banned_users()
        for user_id in users:
            BANNED_USERS.add(user_id)
    except:
        pass
    await app.start()
    for all_module in ALL_MODULES:
        importlib.import_module("RemaxBot.plugins" + all_module)
    LOGGER("RemaxBot.plugins").info(
        "تم استيراد وحدات أوامر ميوزك ريماكس  بنجاح "
    )
    await userbot.start()
    await Remax.start()
    try:
        await Remax.stream_call(
            "http://docs.evostream.com/sample_content/assets/sintel1m720p.mp4"
        )
    except NoActiveGroupCall:
        LOGGER("RemaxBot").error(
            "[خطاء] - \n\n يرجى تشغيل المكالمة الصوتية لمجموعة المسجل الخاصة بك. تأكد من عدم إغلاق/إنهاء المكالمة الصوتية في مجموعة السجل الخاصة بك مطلقًا"
        )
        sys.exit()
    except:
        pass
    await Remax.decorators()
    LOGGER("RemaxBot").info("بدأ تشغيل Remax Music Bot بنجاح")
    await idle()


if __name__ == "__main__":
    loop.run_until_complete(init())
    LOGGER("RemaxBot").info("إيقاف برنامج Remax Music Bot! مع السلامة")
