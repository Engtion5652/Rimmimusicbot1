from callsmusic.callsmusic import client as USER
from pyrogram import filters
from pyrogram.types import Chat, Message, User


@USER.on_message(filters.text & filters.private & ~filters.me & ~filters.bot)
async def pmPermit(client: USER, message: Message):
  await USER.send_message(message.chat.id,"🌸𝗧𝗵𝗶𝘀 𝗜𝘀 𝗠𝘂𝘀𝗶𝗰 𝗔𝘀𝘀𝗶𝘀𝘁𝗮𝗻𝗰𝗲 𝗢𝗙 𝗗𝗲𝘃𝗿𝗮𝗷 𝗠𝘂𝘀𝗶𝗰 𝗣𝗹𝗮𝘆𝗲𝗿\n🌸𝗗𝗲𝘃𝗲𝗹𝗼𝗽𝗲𝗱 𝗕𝘆 𝗛𝗲𝘅𝗼𝗿 𝘅𝗗\n🌸𝗙𝗼𝗿 𝗛𝗲𝗹𝗽 - @Its_Hexor")
  return                        
