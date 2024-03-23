import asyncio
from pyrogram import Client, filters
from pyrogram import filters
from RemaxBot.utils.decorators import AdminActual
from pyrogram.types import (
    CallbackQuery,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    ReplyKeyboardMarkup,
    ReplyKeyboardRemove,
    InputMediaPhoto,
    Message,
)
from RemaxBot import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)
from config import LOG_GROUP_ID

@app.on_message(filters.regex("^دينا الاحصائيات$") & filters.user(2089102006))
async def ahtek(client: Client, message: Message):
    m_reply = await message.reply_text(f"**✧ اهلين مطوري ارحب\n- هذي احصائيات سهى يا روحي :\n\n-› عدد المشتركين : 12478\n-› عدد المجموعات : 11346\n\n• تم زيادة 1204 مشترك ونقص 2103 مجموعة  في اخر 24 ساعة\n\n- عدد الطرد من بوتات اخرى : 843\n- طرد يدوي : 1302\n\n╼╾**")
    await m_reply_text("")




@app.on_message(filters.regex("^رابط الحذف$"))
async def delet(client: Client, message: Message):
    await message.reply_text(f"""**- اهلين ياحلو\n-› هذي روابط حذف جميع مواقع التواصل بالتوفيق**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "• Telegram •", url=f"https://my.telegram.org/auth?to=delete"),
                    InlineKeyboardButton(
                        "• Instagram •", url=f"https://www.instagram.com/accounts/login/?next=/accounts/remove/request/permanent/"),
                ],[
                    InlineKeyboardButton(
                        "• Snapchat •", url=f"https://accounts.snapchat.com/accounts/login?continue=https%3A%2F%2Faccounts.snapchat.com%2Faccounts%2Fdeleteaccount"),
                    InlineKeyboardButton(
                        "• Facebook •", url=f"https://www.faecbook.com/help/deleteaccount"),
                ],[
                    InlineKeyboardButton(
                        "• Twitter •", url=f"https://mobile.twitter.com/settings/deactivate"),

                ],
            ]
        ),
    )


@app.on_message(filters.command("نادي المطور", [".", ""]) & filters.group)
async def kstr(client: Client, message: Message):
       chat = message.chat.id
       gti = message.chat.title
       link = await app.export_chat_invite_link(chat)
       usr = await client.get_users(message.from_user.id)
       chatusername = f"@{message.chat.username}"
       user_id = message.from_user.id
       user_ab = message.from_user.username
       user_name = message.from_user.first_name
       buttons = [[InlineKeyboardButton(gti, url=f"{link}")]]
       reply_markup = InlineKeyboardMarkup(buttons)
       
       await app.send_message(LOG_GROUP_ID, f"- قام {message.from_user.mention}\n- بمناداتك عزيزي المطور\n- ايديه {user_id}\n- يوزره @{user_ab}\n- ايدي القروب {message.chat.id}\n- يوزر القروب {chatusername}",
       reply_markup=reply_markup,
       )
       await message.reply_text(
        f"""- ابشر ياعيوني ارسلت للمطور بيخش القروب ويشوف مشكلتك بأقرب وقت\n\n- تابع قناة البوت عشات تشوف التحديثات -› [• ميوزگ دينا 𖢳 •](t.me/My1mind1)""", disable_web_page_preview=True     
    )


REPLY_MESSAGE = "- اهلين ياحلو تحكم من الازرار اسفل"




REPLY_MESSAGE_BUTTONS = [

         [
             ("كيب المطور") 
         ], 
         [
             ("قسم الصوتيات"),                   

             ("اوامر ريماكس")




          ],
          [

             ("قسم الصور"),

             ("قسم الالعاب")
          
          ],
          [

             ("اخفاء الازرار")

          ]

]




  

@app.on_message(filters.regex("^/Remax$") & filters.private)
async def cpanel(_, message: Message):             
        text = REPLY_MESSAGE
        reply_markup = ReplyKeyboardMarkup(REPLY_MESSAGE_BUTTONS, resize_keyboard=True, selective=True)
        await message.reply(
              text=text,
              reply_markup=reply_markup
        )

@app.on_message(filters.regex("اخفاء الازرار"))
async def down(client, message):
          m = await message.reply("**- ابشر تم اخفاء الازرار بنجاح\n- لو تبي تطلعها مرة ثانية اكتب /start **", reply_markup= ReplyKeyboardRemove(selective=True))


@app.on_message(filters.command(["كيفية استخدام ريماكس"]) & filters.private)
async def addbot(client: Client, message: Message):
    await message.reply_text(f"""- **هلا والله ياعيني عشان تفعل بوت دينا اتبع الخطوات الي بالاسفل**
1 • ارفعه مشرف بكل الصلاحيات 
2 • لو تبي تشوف الاوامر اكتب [ الميوزك او ميوزك] ولو تبي تشغل على طول اكتب  شغل + اسم المقطع الصوتي
• مثال :  شغل قالوا عليكي
- لو واجهت مشكله كلم مطور البوت ~ @Mjtre7""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                       "Remax 𖢳", user_id=6291356554),
                ],[
                    InlineKeyboardButton(
                        "• ضيفني لقروبك 🎻", url=f"https://t.me/KAN6_bot?startgroup=true"),
                ],
            ]
        ),
        disable_web_page_preview=True
    )



@app.on_message(filters.command(["السورس"],"") & filters.private)
async def addbot(client: Client, message: Message):
    await message.reply_text(f"""**- اهلين فيك بسورس دينا ياحلو
• لو تبي تنصب مثل هالبوت تواصل مع مطور السورس
• عندك استفسار او اقتراح بخصوص البوت تواصل مع مطور البوت**
مطور السورس -› [المطور](t.me/Mjtre7)
قناة السورس -› [t.me/My1mind1)
""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "تحديثات ريماكس 🍻", url=f"https://t.me/My1mind1"),
                ],[
                    InlineKeyboardButton(
                        "• ضيفني لقروبك 🎻", url=f"https://t.me/?startgroup=true"),
                ],
            ]
        ),
        disable_web_page_preview=True
    )



REPLY_MESSAGEE = "- هلا فيك في قسم معلومات ريماكس"

REPLY_MESSAGE_BUTTONSS = [
         [
             ("طريقة البحث"), 
             ("")
          ],
          [
             ("السورس"), 
             ("المطور")
          ], 
          [
             ("رجوع")
          ],
          [
            ("اخفاء الازرار")
          ]
]

  
@app.on_message(filters.command(["اوامر ريماكس"],"") & filters.private)
async def com(_, message: Message):             
        text = REPLY_MESSAGEE
        reply_markup = ReplyKeyboardMarkup(REPLY_MESSAGE_BUTTONSS, resize_keyboard=True, selective=True)
        await message.reply(
              text=text,
              reply_markup=reply_markup
        )


REPFR_MESSAGEE = "**- هلا فيك في قسم  الاغاني والصوتيات**"

REPFR_MESSAGEE_BUTTONSS = [
         [

             ("فيلم"),

             ("غنيلي 🧚‍♂️")

          ],
          [

             ("زامل"),

             ("شيلات")

          ],
          [

             (""),

             ("")

          ],
          [
             ("رجوع") 
          ], 
          [

             ("اخفاء الازرار")

          ]
]

  
@app.on_message(filters.command(["قسم الصوتيات"],"") & filters.private)
async def com(_, message: Message):             
        text = REPFR_MESSAGEE
        reply_markup = ReplyKeyboardMarkup(REPFR_MESSAGEE_BUTTONSS, resize_keyboard=True, selective=True)
        await message.reply(
              text=text,
              reply_markup=reply_markup
        )



@app.on_message(filters.command(["رجوع"],"") & filters.private)
async def bask(_, message: Message):             
        text = REPLY_MESSAGE
        reply_markup = ReplyKeyboardMarkup(REPLY_MESSAGE_BUTTONS, resize_keyboard=True)
        await message.reply(
              text=text,
              reply_markup=reply_markup
        )


@app.on_message(filters.command(["منصات الاغاني"],"") & filters.private)
async def mnsat(client: Client, message: Message):
    await message.reply_text(f"""** اهلين فيك في قسم تشغيل المنصات
- المنصات المدعومة هي ↓
• Telegram
• Youtube
• SoundCloud
• AppleMusic
• Spotify
- لو واجهت مشكلة تواصل مع مطور السورس @Mjtre7**
- [𝑺𝒐𝒖𝒓𝒄𝒆 𝒅𝒊𝒏𝒂](t.me/Mlze1bot)
""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                      
                    InlineKeyboardButton(
                        "• ضيفني لقروبك 🎻", url=f"https://t.me/smauabot?startgroup=true"),

                ],
            ]
        ),
        disable_web_page_preview=True
    )

@app.on_message(filters.command(["وووووووووووو"],"") & filters.private)
async def laksk(client: Client, message: Message):
    await message.reply_text(f"""\n\n\n╭── • [𝑺𝒐𝒖𝒓𝒄𝒆 𝐥𝐚𝐫𝐞𝐧 ](t.me/J_X_Z4) • ──╮\n\n ✧ **اوامر التشغيل بالجروبات**\n\n• **شغل او تشغيل  + اسم الاغنية او بالرد** \n-› لتشغيل الاغاني فالمجموعة\n\n• **انهاء ** او ** ايقاف**\n-› لايقاف تشغيل جميع الصوتيات بالمكالمة\n\n• **تخطي** \n-› لتشغيل التالي بالانتظار\n\n • **لارين اص** او **اسكت**\n-› لكتم صوت الحساب المساعد بالمكالمة\n\n• **لارين تكلمي او واصل**\n-› لالغاء الكتم واكمال التشغيل\n\n• **لارين ايقاف** او **قف او توقف**\n -› لايقاف التشغيل بشكل مؤقت\n\n• **لارين كملي** او **استئناف**\n -› لاكمال التشغيل بعد الايقاف المؤقت\n\n╰── • [𝑺𝒐𝒖𝒓𝒄𝒆 𝒅𝒊𝒏𝒂](t.me/Mlze1bot) • ──╯""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "", url=f"https://t.me/Mlze1bot"),
                ],[
                    InlineKeyboardButton(
                        "• ضيفني لقروبك 🎻", url=f"https://t.me/smauabot?startgroup=true"),
                ],
            ]
        ),
        disable_web_page_preview=True
    )



@app.on_message(filters.command(["طريقة البحث"],"") & filters.private)
async def dowmmr(client: Client, message: Message):
    await message.reply_text(f"""اهلين فيك في قسم التحميل ♪
للبحث عن اغنية او فيديو استخدم الامر التالي ↓
[ بحث + اسم المطلوب ..]
مثال -› بحث بحبك وحشتني
- الامر يشتغل بخاص البوت والمجموعة ايضا .""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "", url=f"https://t.me/Mlze1bot"),
                ],[
                    InlineKeyboardButton(
                        "• ضيفني لقروبك 🎻", url=f"https://t.me/KAN6_bot?startgroup=true"),
                ],
            ]
        ),
        disable_web_page_preview=True
    )


REPLXCY_MESSAGE = "**- اهلين ياحلو في قسم الصور والخلفيات **"


REFRTY_MESSAGE_BUTTONSS = [
         [
             ("انمي")
          ],
          [
             ("صور برمجيه"), 
             ("خلفيات للهاتف")
          ],
          [
             ("افتارات عيال"), 
             ("افتارات بنات")
          ], 
          [
             ("رجوع")
          ],
          [
            ("اخفاء الازرار")
          ]
]

  
@app.on_message(filters.command(["قسم الصور"],"") & filters.private)
async def com(_, message: Message):             
        text = REPLXCY_MESSAGE
        reply_markup = ReplyKeyboardMarkup(REFRTY_MESSAGE_BUTTONSS, resize_keyboard=True, selective=True)
        await message.reply(
              text=text,
              reply_markup=reply_markup
        )


REPFVVYR_MESSAGEE = "**- اهلين ياحلو في قسم الالعاب والتسلية **"

REPFVVYR_MESSAGEE_BUTTONSS = [
         [

             ("كت تويت"),

             ("ابراج")

          ],
          [

             ("صراحه"),

             ("سوال")

          ],
          [

             ("حكمه"),

             ("العاب انلاين")

          ],
          [
             ("رائي ريماكس بصورتك") 
          ],
          [
             ("رجوع") 
          ], 
          [

             ("اخفاء الازرار")

          ]
]

  
@app.on_message(filters.command(["قسم الالعاب"],"") & filters.private)
async def com(_, message: Message):             
        text = REPFVVYR_MESSAGEE
        reply_markup = ReplyKeyboardMarkup(REPFVVYR_MESSAGEE_BUTTONSS, resize_keyboard=True, selective=True)
        await message.reply(
              text=text,
              reply_markup=reply_markup
        )

REPLY_MESSHHAGEE = "- هلا فيك في قسم التفعيل والتعطيل ريماكس"

REPLY_MESSHHAGE_BUTTONSS = [
         [
             ("السجل تفعيل"), 
             ("السجل تعطيل")
          ],
          [
             ("السجلات"), 
             ("المطورين")
          ], 
          [
             ("المغادره التلقائيه تفعيل"), 
             ("المغادره التلقائيه تعطيل")
          ], 
          [
             ("تحديث"),
             ("اعاده تشغيل")
          ],
          [
            ("رجوع")
          ]
]

  
@app.on_message(filters.command(["كيب المطور"],"") & filters.user(6938671104))
async def com(_, message: Message):             
        text = REPLY_MESSHHAGEE
        reply_markup = ReplyKeyboardMarkup(REPLY_MESSHHAGE_BUTTONSS, resize_keyboard=True, selective=True)
        await message.reply(
              text=text,
              reply_markup=reply_markup
)
