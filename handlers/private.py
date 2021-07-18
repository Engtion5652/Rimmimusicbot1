from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from config import BOT_NAME as bn
from helpers.filters import other_filters2


@Client.on_message(other_filters2)
async def start(_, message: Message):
    await message.reply_sticker("CAACAgEAAxkBAAIN52Dz6RgJs3LErFPsRpFt_ZdmdjH5AAILAQACT_MRR6hWRja4ZrgeIAQ")
    await message.reply_text(
        f"""**ʜᴇʟʟᴏ ᴡᴇʟᴄᴏᴍᴇ ᴛᴏ ᴇꜱᴘᴏʀᴛ ᴍᴜꜱɪᴄ ʙᴏᴛ🌹

🌼ᴛʜɪꜱ ʙᴏᴛ ᴍᴀᴅᴇ ʙʏ @Its_Hexor & @Sanki_Owner\n⭐ᴘʀᴏꜰᴇꜱꜱɪᴏɴᴀʟ ᴀɴᴅ ꜱᴜᴘᴇʀ-ꜰᴀꜱᴛ ᴛᴇʟᴇɢʀᴀᴍ ᴠᴄ ʙᴏᴛ\n\nꜰᴏʀ ᴍᴏʀᴇ ʜᴇʟᴘ [❰ᴄʟɪᴄᴋ❱](https://t.me/esportcheater).

✌ᴇꜱᴘᴏʀᴛ✘ᴄʟᴀɴ ᴏꜰꜰɪᴄɪᴀʟ ᴍᴜꜱɪᴄ ʙᴏᴛ**
        """,
        reply_markup=InlineKeyboardMarkup(
            [
      [
                    InlineKeyboardButton(
                        "❰ᴇꜱᴘᴏʀᴛ✘ᴄʟᴀɴ❱", url="https://t.me/esportcheater"
                    ),
                    InlineKeyboardButton(
                        "❰ꜱᴜᴘᴘᴏʀᴛ❱", url="https://t.me/SankiPublicEnjoy"
                    )
                ]
            ]
        ),
     disable_web_page_preview=True
    )

@Client.on_message(filters.command("status") & ~filters.private & ~filters.channel)
async def gstart(_, message: Message):
      await message.reply_text("""**ɢʀᴏᴜᴘ ᴍᴜꜱɪᴄ ᴘʟᴀʏᴇʀ ᴏɴʟɪɴᴇ ✅**""",
      reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        " ᴏᴡɴᴇʀ", url="https://t.me/Its_Hexor")
                ]
            ]
        )
   )





