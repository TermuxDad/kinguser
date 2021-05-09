from pyrogram import filters, Client
from kingbot import kingbot, AdminSettings , HNDLR
from time import time

_MODULE__ = "PING"
__HELP__ = """
__**This command helps you to instantly get the ping of the userbot**__
──「 **Usage** 」──
-> `ping`
"""
@kingbot.on_message(filters.command("ping",HNDLR) & filters.user(AdminSettings))
async def pinger(_, message):
    start = time.now()
    await message.edit('`Pong!`')
    end = time.now()
    m_s = (end - start).microseconds / 1000
    await message.edit(f"**Pong!**\n`{m_s} ms`")
