from pyrogram import client , filters
from pyrogram.types import Message
from kingbot import kingbot , AdminSettings, HNDLR
__MODULE__ = "start"
__HELP__ = """**Just a start message**
"""
@kingbot.on_message(filters.command(commands:"start",prefixes:HNDLR) & filters.user(AdminSettings))
async def start(_, message: Message):
    await message.reply_text(
        "Shit u are allowed dear!! \n Only Kings wield this power" )
