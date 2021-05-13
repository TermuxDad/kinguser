from pyrogram import client, filters
import asyncio
import time
from pyrogram.types import ChatPermissions
from kingbot import kingbot, vr ,Adminsettings
from carbonnow import Carbon

__MODULE__ = "carbon"
__HELP__ = """
__**This command helps you to generate carbon of a text(program) in the chat**__
──「 **Usage** 」──
-> `carbon`
"""

@kingbot.on_message(filters.command("carbon",vr.get("HNDLR")) & filters.user(Adminsettings))  
async def carbon(_, message):
    msg_text=message.text
    chat_id=message.chat.id
    if message.reply_to_message:
        reply_text=message.reply_to_message.text
        carbon = Carbon(
            code=reply_text,
        )
        try:
            await carbon.save('carbon_photo')
        finally:
            await kingbot.send_photo(chat_id ,"carbon_photo.jpg" , caption="Generated from King Userbot")
    else:
        await message.reply("Reply to a text to convert !!")
