from uti.misc import paginate_modules
from pyrogram import idle
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton , InlineQuery ,Message, CallbackQuery, InlineQueryResultPhoto
from pyrogram import filters 
from kingbot import kingbot ,setbot , vr,Adminsettings
from uti.serra import ser
import re
Admins= Adminsettings
@kingbot.on_message(filters.command("help",".") & filters.user(1359459092))
async def h_lp(_ , message):
  res=await kingbot.get_inline_bot_results("Devilkalund2bot", "hlpin")
  await kingbot.send_inline_bot_result(message.chat.id, res.query_id, res.results[0].id)
@setbot.on_inline_query(filters.regex("hlpin"))
async def in_h_lp(_ , inline_query):
  keboard= InlineKeyboardMarkup(
                  [  [
                        InlineKeyboardButton(
                            "Group Admin Plugins",
                            callback_data= "_admin_h"
                        )
                    ],
                    [
                        InlineKeyboardButton(
                            "Util Plugins",
                            callback_data= "_util_h"
                        ),
                        InlineKeyboardButton(
                            "ASSISTANT Plugins",
                            callback_data= "_ast_h"
                        )
                    ],
                    [
                        InlineKeyboardButton(
                            "OWNER Plugins",
                            callback_data= "_own_h"
                        )
                    ],
                    [
                        InlineKeyboardButton(
                            "Close the menu",
                            callback_data= "kloz"
                  )]])
  await inline_query.answer(
        results=[
            InlineQueryResultPhoto(
                photo_url= "https://telegra.ph/file/7b7141557ddf084e0afe6.jpg",
                title="Help",
                caption=f"You are accessing help for **King Userbot** \n __Everyone is a king. Until the real king arrives.__",
                reply_markup=keboard,
            ),
        ]
    )
def cowner(func):
        async def wrapper(_, cbq: CallbackQuery):
            if cbq.from_user.id in AdminSettings:
                pass
            else:
                userr = await setbot.get_user(Owner)
                await cbq.answer(
                    f"Only {userr.first_name} Can Access this...! Get yourself a Userbot🤘",
                    show_alert=True)
        return wrapper

@setbot.on_callback_query(filters.user(1359459092))
async def cbire(_ , cbq: CallbackQuery):
   HELP_COMMANDU = ser.HU
   HELP_COMMANDA = ser.HA
   HELP_COMMANDO = ser.HO
   HELP_COMMANDAST = ser.HAT
   HELP_COMMANDS = ser.HC
   print(cbq) 
   cid=cbq.id
   cdt=cbq.data
   if cdt == "_admin_h":
      keyboard = paginate_modules(0, HELP_COMMANDA, "help")
      keyboard.append([InlineKeyboardButton(
                            "Back",
                            callback_data= "b_k"
             )])
      keyboard.append([InlineKeyboardButton(
                            "Close",
                            callback_data= "kloz"
             )])
      await cbq.edit_message_caption(
                            caption=f"This is the help for admin commmands to manage your group efficiently",
                            )
      await cbq.edit_message_reply_markup(reply_markup=InlineKeyboardMarkup(keyboard))
   if cdt == "_util_h":
      keyboard = paginate_modules(0, HELP_COMMANDU, "help")
      keyboard.append([InlineKeyboardButton(
                            "Back",
                            callback_data= "b_k"
             )])
      keyboard.append([InlineKeyboardButton(
                            "Close",
                            callback_data= "kloz"
             )])
      await cbq.edit_message_caption(
                            caption="This is the help for util commmands to make your life easy peasy",
                            )
      await cbq.edit_message_reply_markup(reply_markup=InlineKeyboardMarkup(keyboard))
   if cdt == "_ast_h":
      keyboard = paginate_modules(0, HELP_COMMANDAST, "help")
      keyboard.append([InlineKeyboardButton(
                            "Back",
                            callback_data= "b_k"
             )])
      keyboard.append([InlineKeyboardButton(
                            "Close",
                            callback_data= "kloz"
             )])
      await cbq.edit_message_caption(
                            caption="This is the help for assistant commmands to manage your userbot",
                            )
      await cbq.edit_message_reply_markup(reply_markup=InlineKeyboardMarkup(keyboard))
   if cdt == "_own_h":
      keyboard =   paginate_modules(0, HELP_COMMANDO, "help")
      keyboard.append([InlineKeyboardButton(
                            "Back",
                            callback_data= "b_k"
             )])
      keyboard.append([InlineKeyboardButton(
                            "Close",
                            callback_data= "kloz"
             )])
      await cbq.edit_message_caption(
                            caption="This is the help for owner commmands ",
                            )
      await cbq.edit_message_reply_markup(reply_markup=InlineKeyboardMarkup(keyboard))
   if cdt == "b_k":
        keyboard=[[InlineKeyboardButton(
                            "Group Admin Plugins",
                            callback_data= "_admin_h"
                        )],
                        [InlineKeyboardButton(
                            "Util Plugins",
                            callback_data= "_util_h"
                        ),
                        InlineKeyboardButton(
                            "ASSISTANT Plugins",
                            callback_data= "_ast_h"
                        )],
                        [InlineKeyboardButton(
                            "OWNER Plugins",
                            callback_data= "_own_h"
                        )],
                        [InlineKeyboardButton(
                            "Close",
                            callback_data= "kloz"
                  )]]
        await cbq.edit_message_caption(
                            caption=f"You are accessing help for **King Userbot** \n __Everyone is a king. Until the real king arrives.__",
                            )
        await cbq.edit_message_reply_markup(reply_markup=InlineKeyboardMarkup(keyboard))
   if cdt == "kloz":
        await kingbot.delete_messages(chat_id=cbq.message.chat.id,message_ids=cbq.message.message_id)
   await kingbot.send_message("me", "got query") 
   HELP_COMMANDS = ser.HC 
   mod_match = re.match(r"help_module\((.+?)\)", cbq.data)
   data=cbq.data
   module=data[data.index("(")+1:len(data)-1]
   back_match = re.match(r"help_back", cbq.data)
   await kingbot.send_message("me",(str(Admins)))
   if mod_match:
        if module in HELP_COMMANDS:
           await kingbot.send_message("me" , "SUCCESS")
           modulee= module
        else:
           await kingbot.send_message("me" , "ELSE")
           return
        text = (
            "This is help for the plugins **{}**:\n".format(
                modulee
            )
            + HELP_COMMANDS[modulee]
        )

        await cbq.edit_message_caption(caption=text)
        await cbq.edit_message_reply_markup(
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(
                            text="Back",    
                            callback_data="help_back"
                        )
                    ]
                ]
            )
        )
                  

   elif back_match:
        keyboard=[[InlineKeyboardButton(
                            "Group Admin Plugins",
                            callback_data= "_admin_h"
                        )],
                        [InlineKeyboardButton(
                            "Util Plugins",
                            callback_data= "_util_h"
                        ),
                        InlineKeyboardButton(
                            "ASSISTANT Plugins",
                            callback_data= "_ast_h"
                        )],
                        [InlineKeyboardButton(
                            "OWNER Plugins",
                            callback_data= "_own_h"
                        )],
                        [InlineKeyboardButton(
                            "Close",
                            callback_data= "kloz"
                  )]]
        await cbq.edit_message_caption(
                            caption=f"You are accessing help for **King Userbot** \n __Everyone is a king. Until the real king arrives.__",
                            )
        await cbq.edit_message_reply_markup(reply_markup=InlineKeyboardMarkup(keyboard))
   await cbq.answer()
# async def help_button_callback(_, __, query):
#     if re.match(r"help_", query.data):
#         return True


# help_button_create = filters.create(help_button_callback)
#@setbot.on_callback_query(filters.user(1359459092))
#async def help_button(_, query):  


