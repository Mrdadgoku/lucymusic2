from callsmusic.callsmusic import client as USER
from pyrogram import filters
from pyrogram.types import Chat, Message, User


@USER.on_message(filters.text & filters.private & ~filters.me & ~filters.bot)
async def pmPermit(client: USER, message: Message):
  await USER.send_message(message.chat.id,"Hello my name is ˹ ᴬᴺᴺᴵᴱ ✘ ᴍᴜsɪᴄ˼ ♪™➜ I am play music on group first add lucy bot to your group and make admin and play songs")
  return                        
