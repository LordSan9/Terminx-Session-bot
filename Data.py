from pyrogram.types import InlineKeyboardButton


class Data:
    # Start Message
    START = """
⌯¦مرحبـاً بـك عزيـزي 📬 {}
⌯¦في بــوت استـخـراج جلـسـة
⌯¦استـخـراج تيرمـكـس تليثون
⌯¦وبــايــروجـرام للـمـيــوزك🎧
- يعمـل هـذا البـوت لمساعدتـك بطريقـة سهلـه للحصـول على كـود تيرمكـس لتشغيل تلـيثون والبايروجرام لتشغيل سـورس اغــاني تم انشـاء هـذا البـوت بواسطـة:  [⌯DEV EITHON⌯](https://t.me/TTTLL0)
    """

    # Home Button
    home_buttons = [
        [InlineKeyboardButton("🌐¦اضـغـط لـبـدا استـخـراج كــود", callback_data="generate")],
        [InlineKeyboardButton(text="🔙رجوع", callback_data="home")]
    ]

    generate_button = [
        [InlineKeyboardButton("🌐¦اضـغـط لـبـدا استـخـراج كــود", callback_data="generate")]
    ]

    # Rest Buttons
    buttons = [
        [InlineKeyboardButton("🌐¦اضـغـط لـبـدا استـخـراج كــود", callback_data="generate")],
        [InlineKeyboardButton("• DE⃟V EITHON •", url="https://t.me/TTTLL0"),
         InlineKeyboardButton("• قناة السورس •", url="https://t.me/EITHON1") 
        ],
        [
            InlineKeyboardButton("❓¦طـريـقـه الاسـتـخـدام", callback_data="help"),
            InlineKeyboardButton("💾¦مـعـلومـات", callback_data="about")
      ],
        [InlineKeyboardButton("⚙️¦الــســـورس", url="https://t.me/EITHON1")],
    ]


    # Help Message
    HELP = """
**📚¦الاوامــر الـمتـاحـه**
/about - معلومات البوت
/help - طريقه استخدامي
/start - حتى تشغل البوت
/generate - حتى تبدا بأستخراج كود
/cancel - لألغاء الاستخراج
/restart - اعادة تشغيل البوت
"""

    # About Message
    ABOUT = """
**💾¦مـعـلومـات** 
⚡¦بـوت استخـراج كـود تيرمكـس خـاص بســورس التليـثون وكــود بـايــروجـرام خـاص بـسـورس الـمـيـوزك🎶

🌀¦قـنـاه الـبـوت : [⌯𝗦𝗢𝗨𝗥𝗖𝗘 Ξ𝗜𝗧𝗛𝗢𝗡™⌯](EITHON1)

🌏¦اللـغــه : [بـايـثـون](www.python.org)

👨🏼‍💻¦الـمـبـرمــج : @TTTLL0
    """
