from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from SHUKLAMUSIC import app
from config import BOT_USERNAME
from SHUKLAMUSIC.utils.errors import capture_err
import httpx 
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

start_txt = """
𝐏ʟᴇᴀꜱᴇ 𝐂ʟɪᴄᴋ 𝐎ɴ 𝐒ᴏᴜʀᴄᴇ 𝐂ᴏᴅᴇ 𝐁ᴜᴛᴛᴏɴ 𝐁ᴇʟᴏᴡ !
<pre>||➥ᴜᴘᴛɪᴍᴇ: 𝟷ʜ:𝟹𝟺ᴍ:𝟻𝟺s
➥sᴇʀᴠᴇʀ sᴛᴏʀᴀɢᴇ: 𝟸𝟽.𝟺%
➥ᴄᴘᴜ ʟᴏᴀᴅ: 𝟷𝟷.𝟸%
➥ʀᴀᴍ ᴄᴏɴsᴜᴍᴘᴛɪᴏɴ: 𝟷𝟽.𝟻%||</pre>
•──────────────────•
ᴘᴏᴡєʀєᴅ ʙʏ»|| [ᴍᴀᴅᴀʀᴀ](https://t.me/YOUR_fucker_dad)||
•──────────────────•
"""

@app.on_message(filters.command("repo"))
async def start(_, msg):
    buttons = [
        [
            InlineKeyboardButton(text=" ˹ηєᴛᴡᴏʀᴋ˼ ", url="https://t.me/+dv_rcq5uIXhmMWM1",),
            InlineKeyboardButton(text=" ˹ϻʏ ʜᴏϻє˼ ", url="https://t.me/+Imyf3M9TO5k1ODRl",),
        ],
        
     [
            InlineKeyboardButton("˹ᴘʀιᴠᴧᴄʏ˼", url=f"https://telegra.ph/Privacy-Policy-08-03-101"),
            InlineKeyboardButton("𝐒ᴏᴜʀᴄᴇ 𝐂ᴏᴅᴇ", url=f"https://files.catbox.moe/k3ywrd.mp4"),
        ],
        
          [
            InlineKeyboardButton("˹ ϻʏ ϻᴧsᴛєʀ ˼ 👑", url="https://t.me/YOUR_MADARA_BRO"),
          ]]
    
    reply_markup = InlineKeyboardMarkup(buttons)
    
    await msg.reply_photo(
        photo="https://files.catbox.moe/5go4t6.jpg",
        caption=start_txt,
        reply_markup=reply_markup
    )
