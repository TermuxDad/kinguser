from datetime import datetime
from kingbot import kingbot, setbot , vr, Adminsettings
from pyrogram import filters
from pyrogram.types import Messages
__MODULE__ = "Stats"
__HELP__="""
`stats` gives you your current stats i.e. Your group , channel , adminship and bot count
"""
@kingbot.on_message(filters.command("help",vr.get("HNDLR"))  & filters.user(Adminsettings))
async def stats(_, message):
    message.edit_text("Collecting stats")
    start = datetime.now()
    u = 0
    g = 0
    sg = 0
    c = 0
    b = 0
    a_chat = 0
    group = ["supergroup", "group"]
    async for dialog in kingbot.iter_dialogs():
        if dialog.chat.type == "private":
            u += 1
        elif dialog.chat.type == "bot":
            b += 1
        elif dialog.chat.type == "group":
            g += 1
        elif dialog.chat.type == "supergroup":
            sg += 1
            user_s = await dialog.chat.get_member(int(client.me.id))
            if user_s.status in ("creator", "administrator"):
                a_chat += 1
        elif dialog.chat.type == "channel":
            c += 1

    end = datetime.now()
    ms = (end - start).seconds
    await message.edit_text(
        """`Your Stats Obtained in {} seconds`
`You have {} Private Messages.`
`You are in {} Groups.`
`You are in {} Super Groups.`
`You Are in {} Channels.`
`You Are Admin in {} Chats.`
`Bots = {}`""".format(
            ms, u, g, sg, c, a_chat, b
        )
    )
