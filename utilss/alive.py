from pyrogram import client, filters
import asyncio
import time
from pyrogram.types import ChatPermissions
from kingbot import kingbot, vr ,Adminsettings
__MODULE__ = "alive"
__HELP__ = """
__**This command helps you to check wether userbot is alive**__
──「 **Usage** 」──
-> `alive`
"""

@kingbot.on_message(filters.command("alive",vr.get("HNDLR")) & filters.user(Adminsettings))  
async def alive(_, message):
    await message.reply(
        f"`You expected me to be dead 😈! {message.from_user.first_name} , I am Alive 🤟`"
    )