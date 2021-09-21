
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from config import BOT_NAME as bn
from helpers.filters import other_filters2


@Client.on_message(other_filters2)
async def start(_, message: Message):
    
    await message.reply_text(
        f"""**
🌠𝗧𝗵𝗶𝘀 𝗜𝘀 𝗔𝗱𝘃𝗮𝗻𝗰𝗲 𝗧𝗲𝗹𝗲𝗴𝗿𝗮𝗺 𝗠𝘂𝘀𝗶𝗰 𝗕𝗼𝘁 \n🌺𝗥𝘂𝗻 𝗢𝗻 𝗣𝗿𝗶𝘃𝗮𝘁𝗲 𝗩𝗣𝗦 𝗦𝗲𝗿𝘃𝗲𝗿 \n🌼𝗙𝗲𝗲𝗹 𝗛𝗶𝗴𝗵 𝗤𝘂𝗮𝗹𝗶𝘁𝘆 𝗠𝘂𝘀𝗶𝗰 𝗜𝗻 𝗩𝗖 \n⭐𝗗𝗲𝘃𝗲𝗹𝗼𝗽𝗲𝗱 𝗕𝘆 [🕊️⃝🇮🇳★𝙍𝙤𝙮𝙖𝙡❤️𝙃𝙚𝙖𝙧𝙩★🇮🇳⃝🕊️](https://t.me/Royals_heart)**
        """,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "😈🤟❰𝗢𝘄𝗻𝗲𝗿❱😎😈", url="https://t.me/Royals_heart")
                  ],[
                    InlineKeyboardButton(
                        "🇮🇳❰𝗦𝘂𝗽𝗽𝗼𝗿𝘁❱🇮🇳", url="https://t.me/Dil_dosti_duniya_dari"
                    ),
                    InlineKeyboardButton(
                        "🥰❰𝗚𝗿𝗼𝘂𝗽❱🥰", url="https://t.me/Dil_dosti_duniya_dari"
                    )
                ],[ 
                    InlineKeyboardButton(
                        "😁❰𝗖𝗼𝗺𝗺𝗮𝗱𝘀❱😁", url="https://telegra.ph/Commands-For---Devil-Hacker-Music-09-17"
                    )]
            ]
        ),
     disable_web_page_preview=True
    )

@Client.on_message(filters.command("Royal") & ~filters.private & ~filters.channel)
async def gstart(_, message: Message):
      await message.reply_text("""**🕊️⃝🦋𝙍𝙞𝙢𝙢𝙞➳𝙈𝙪𝙨𝙞𝙘➳𝘽𝙤𝙩🕊️⃝🦋 𝗠𝘂𝘀𝗶𝗰 𝗕𝗼𝘁 𝗢𝗻𝗹𝗶𝗻𝗲 𝗡𝗼𝘄\n🌠 @Royals_heart <3**""",
      reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🌼𝗦𝘂𝗽𝗽𝗼𝗿𝘁", url="https://t.me/Dil_dosti_duniya_dari")
                ]
            ]
        )
   )
