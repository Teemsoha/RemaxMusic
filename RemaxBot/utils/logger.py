from pyrogram.enums import ParseMode

from RemaxBot import app
from RemaxBot.utils.database import is_on_off
from config import LOG_GROUP_ID, MUSIC_BOT_NAME


async def play_logs(message, streamtype):
    if await is_on_off(2):
        logger_text = f"""
** {MUSIC_BOT_NAME} تشغيل جديد **

**ايدي الجروب* <code>{message.chat.id}</code>
**اسم الجروب :** {message.chat.title}
**معرف الجروب :** @{message.chat.username}

** ايدي الي شغل :** <code>{message.from_user.id}</code>
** اسمه :** {message.from_user.mention}
** معرفه :** @{message.from_user.username}

** بعنوان :** {message.text.split(None, 1)[1]}
** منصة التشغيل :** {streamtype}"""
        if message.chat.id != LOG_GROUP_ID:
            try:
                await app.send_message(
                    chat_id=LOG_GROUP_ID,
                    text=logger_text,
                    parse_mode=ParseMode.HTML,
                    disable_web_page_preview=True,
                )
            except:
                pass
        return
