from pyrogram import client, filters
import asyncio
import time
from emoji import get_emoji_regexp
from kingbot import edrep, kingbot , AdminSettings ,HNDLR

__MODULE__ = "chat link"
__HELP__ = """
__**This command helps you to instantly get the invite link of the chat**__
──「 **Usage** 」──
-> `admins`
"""



@kingbot.on_message(filters.command(start,HNDLR) & filters.user(AdminSettings))
async def invite_link(client, message):
    if message.chat.type in ["group", "supergroup"]:
        chat_name = message.chat.title
        can_invite = await admin_check(message)
        if can_invite:
            try:
                link = await kingbot.export_chat_invite_link(message.chat.id)
                await edrep(message, text=("invite_link").format(chat_name, link))
            except Exception as e:
                print(e)
                await edrep(message, text=("denied_permission"))
    else:
        await message.delete()
