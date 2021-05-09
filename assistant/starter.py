from pyrogram import client , filters
from pyrogram.types import Message
from kingbot import kingbot 
__MODULE__ = "start"
__HELP__ = """**Just a start message**
"""
HNDLR="."
AdminSettings= [1359459092]
@kingbot.on_message(filters.command("start",HNDLR) & filters.user(AdminSettings))
async def start(_, message: Message):
    await message.reply_text(
        "Shit u are allowed dear!! \n Only Kings wield this power" )
