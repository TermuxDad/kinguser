from pyrogram import client, filters
import asyncio
import time
from pyrogram.types import ChatPermissions
from kingbot import kingbot, vr ,Adminsettings
__MODULE__ = "deleteuserhistory"
__HELP__ = """
__**This command helps you to delete all messages from a user in the chat**__
──「 **Usage** 」──
-> `deleteuserhistory`
"""

@kingbot.on_message(filters.group & filters.command("deleteuserhistory",vr.get("HNDLR")) & filters.user(Adminsettings))  
def delete_user_history(_ , message):
    chat_id=message.chat.id
    msg_id=message.message_id
    chat_msg=message.text
    username=None

    if "@" in chat_msg:
        index=chat_msg.index("@")     
        chat_msg=str(chat_msg)
        username=chat_msg[index+1:len(chat_msg)]
    else:                   
        username=message.reply_to_message.from_user.id

    can_delete=kingbot.get_chat_member(chat_id , "me").can_delete_messages
    if(can_delete):      
        client.delete_user_history(chat_id , username)
    else:
        reply_string="Noob,you can't delete their existence !"
        kingbot.edit_message_text(chat_id , msg_id , reply_string )
