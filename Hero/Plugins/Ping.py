import os
import time
from datetime import datetime

import psutil
from pyrogram import Client, filters
from pyrogram.types import Message

from Hero import BOT_USERNAME, MUSIC_BOT_NAME, app, boottime
from Hero.Utilities.ping import get_readable_time

__MODULE__ = "ᴘɪɴɢ"
__HELP__ = """

`/ping` - ᴄʜᴇᴄᴋ ɪғ ʙᴏᴛ ɪs ᴀʟɪᴠᴇ ᴏʀ ɴᴏᴛ.
"""


async def bot_sys_stats():
    bot_uptime = int(time.time() - boottime)
    cpu = psutil.cpu_percent(interval=0.5)
    mem = psutil.virtual_memory().percent
    disk = psutil.disk_usage("/").percent
    stats = f"""
ᴜᴘᴛɪᴍᴇ: {get_readable_time((bot_uptime))}
ᴄᴘᴜ: {cpu}%
ʀᴀᴍ: {mem}%
ᴅɪsᴋ: {disk}%
𝐏𝐎𝐖𝐄𝐑𝐄𝐃 𝐁𝐘: {[𝐊𝐀𝐀𝐋](@ITS_HEAVEN_KING)}"""
    return stats


@app.on_message(filters.command(["ping", f"ping@{BOT_USERNAME}"]))
async def ping(_, message):
    start = datetime.now()
    response = await message.reply_photo(
        photo="https://telegra.ph/file/13bccc62e5a1531ed8988.jpg",
        caption="🌸 ᴘɪɴɢ...",
    )
    uptime = await bot_sys_stats()
    end = datetime.now()
    resp = (end - start).microseconds / 1000
    await response.edit_text(
        f"**💐 ᴘᴏɴɢ**\n`⚡{resp} ᴍs`\n\n**𝐊𝐀𝐀𝐋 𝐌𝐔𝐒𝐈𝐂 sʏsᴛᴇᴍ sᴛᴀᴛs:**{uptime}"
    )
