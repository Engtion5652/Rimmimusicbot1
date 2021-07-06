from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from config import BOT_NAME as bn
from helpers.filters import other_filters2


@Client.on_message(other_filters2)
async def start(_, message: Message):
       await message.reply_text(
        f"""**ᴡᴇʟᴄᴏᴍᴇ ᴛᴏ ᴇꜱᴘᴏʀᴛ ᴍᴜꜱɪᴄ ᴘʟᴀʏᴇʀ

ᴇꜱᴘᴏʀᴛ ᴍᴜꜱɪᴄ ʙᴏᴛ ʜᴏꜱᴛ ᴏɴ ꜰɪʀᴇʙᴀꜱᴇ ꜱᴇʀᴠᴇʀ. ᴜꜱɪɴɢ ᴅᴀᴛᴀʙᴀꜱᴇ ɴᴏ ʟᴀɢ ꜰᴜʟʟ ᴍᴀꜱᴛɪ🎶[🌹| ᴇꜱᴘᴏʀᴛ ᴄʟᴀɴ |🌹](https://t.me/EsportCheater).

ᴛʜɪꜱ ʙᴏᴛ ʜᴏꜱᴛ ᴏɴ ᴘʀɪᴠᴀᴛᴇ ꜱᴇʀᴠᴇʀ!**
        """,
        reply_markup=InlineKeyboardMarkup(
            [
                   [
                    InlineKeyboardButton(
                        "⭐ ɢʀᴏᴜᴘ", url="https://t.me/EsportCheater"
                    ),
                    InlineKeyboardButton(
                        "🌹 ᴏᴡɴᴇʀ", url="https://t.me/its_Hexor"
                    )
                ]
            ]
        ),
     disable_web_page_preview=True
    )

        )
   )





