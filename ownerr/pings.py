from pyrogram import filters, Client
from kingbot import kingbot
from datetime import datetime

__MODULE__ = "PING"
__HELP__ = """
__**This command helps you to instantly get the ping of the userbot**__
──「 **Usage** 」──
-> `ping`
"""
HNDLR="."
AdminSettings= [1359459092]
@kingbot.on_message(filters.command("ping",HNDLR) & filters.user(AdminSettings))
async def pinger(_, message):
    uptime = get_readable_time((time.time() - start_time))
    start = datetime.now()
    end = datetime.now()
    ms = (end - start).microseconds / 1000
    await message.edit_text(
        f"**█▀█ █▀█ █▄░█ █▀▀ █ \n█▀▀ █▄█ █░▀█ █▄█ ▄**\n ➲ `{ms}` \n ➲",
    )
