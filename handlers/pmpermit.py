from callsmusic.callsmusic import client as USER
from pyrogram import filters
from pyrogram.types import Chat, Message, User


@USER.on_message(filters.text & filters.private & ~filters.me & ~filters.bot)
async def pmPermit(client: USER, message: Message):
  await USER.send_message(message.chat.id,"🌸𝗧𝗵𝗶𝘀 𝗜𝘀 𝗠𝘂𝘀𝗶𝗰 𝗔𝘀𝘀𝗶𝘀𝘁𝗮𝗻𝗰𝗲 𝗢𝗙 ❰🕊️⃝🦋𝙍𝙞𝙢𝙢𝙞➳𝙈𝙪𝙨𝙞𝙘➳𝘽𝙤𝙩🦋○🕊️❱❰@RimmiMusicBot❱\n🌸𝗗𝗲𝘃𝗲𝗹𝗼𝗽𝗲𝗱 𝗕𝘆 ❰🕊️⃝🇮🇳★𝙍𝙤𝙮𝙖𝙡❤️𝙃𝙚𝙖𝙧𝙩★🇮🇳⃝🕊️❱❰@royals_heart❱\n🌸𝗙𝗼𝗿 𝗛𝗲𝗹𝗽 𝐆𝐫𝐨𝐮𝐩 - @Dil_dosti_duniya_dari")
  return                        
