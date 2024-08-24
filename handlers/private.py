from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from config import BOT_NAME as bn
from helpers.filters import other_filters2


@Client.on_message(other_filters2)
async def start(_, message: Message):
    
    await message.reply_text(
        f"""**
🌠𝗧𝗵𝗶𝘀 𝗜𝘀 𝗔𝗱𝘃𝗮𝗻𝗰𝗲 𝗧𝗲𝗹𝗲𝗴𝗿𝗮𝗺 𝗠𝘂𝘀𝗶𝗰 𝗕𝗼𝘁 \n🌺𝗥𝘂𝗻 𝗢𝗻 𝗣𝗿𝗶𝘃𝗮𝘁𝗲 𝗩𝗣𝗦 𝗦𝗲𝗿𝘃𝗲𝗿 \n🌼𝗙𝗲𝗲𝗹 𝗛𝗶𝗴𝗵 𝗤𝘂𝗮𝗹𝗶𝘁𝘆 𝗠𝘂𝘀𝗶𝗰 𝗜𝗻 𝗩𝗖 \n⭐𝗗𝗲𝘃𝗲𝗹𝗼𝗽𝗲𝗱 𝗕𝘆 [𝗚𝗢𝗞𝗨🇽𝐄𝐝𝐢𝐭𝐢𝐨𝐧™श्रीराम](https://t.me/GOKUxEDITION)**
        """,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "❰𝗢𝘄𝗻𝗲𝗿❱", url="https://t.me/GOKUxEDITION")
                  ],[
                    InlineKeyboardButton(
                        "❰𝗦𝘂𝗽𝗽𝗼𝗿𝘁❱", url="https://t.me/GOKUxMODZ"
                    ),
                    InlineKeyboardButton(
                        "❰𝗚𝗿𝗼𝘂𝗽❱", url="https://t.me/GOKUxENGINE"
                    )
                ],[ 
                    InlineKeyboardButton(
                        "❰𝗦𝗼𝘂𝗿𝗰𝗲❱", url="https://github.com/Mrdadgoku/lucymusic2"
                    )]
            ]
        ),
     disable_web_page_preview=True
    )

@Client.on_message(filters.command("hexor") & ~filters.private & ~filters.channel)
async def gstart(_, message: Message):
      await message.reply_text("""**ᴬᴺᴺᴵᴱ 𝗠𝘂𝘀𝗶𝗰 𝗕𝗼𝘁 𝗢𝗻𝗹𝗶𝗻𝗲 𝗡𝗼𝘄\n💙˹ ᴬᴺᴺᴵᴱ ✘ ᴍᴜsɪᴄ˼ ♪™➜**""",
      reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🌼𝗦𝘂𝗽𝗽𝗼𝗿𝘁", url="https://t.me/GOKUxEDITION")
                ]
            ]
        )
   )
