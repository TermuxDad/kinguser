from uti.misc import paginate_modules
from pyrogram import idle
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton , InlineQuery ,Message, CallbackQuery, InlineQueryResultPhoto
from pyrogram import filters 
from kingbot import kingbot ,setbot , vr

import re
HNDLR="."
AdminSettings= [1359459092]

@kingbot.on_message(filters.command("help",HNDLR) & filters.user(AdminSettings))
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
        async def wrapper(_, c_q: CallbackQuery):
            if c_q.from_user.id in AdminSettings:
                try:
                    await func(c_q)
                except MessageNotModified:
                    await c_q.answer("Nothing Found to Refresh 🤷‍♂️", show_alert=True)
                except MessageIdInvalid:
                    await c_q.answer("Sorry, I Don't Have Permissions to edit this 😔",
                                     show_alert=True)
            else:
                userr = await setbot.get_user(Owner)
                await c_q.answer(
                    f"Only {userr.first_name} Can Access this...! Get yourself a Userbot🤘",
                    show_alert=True)
        return wrapper

@setbot.on_callback_query(filters.user(AdminSettings))
@cowner
async def cbire(_ , cbq: CallbackQuery):
   from kingbot.__main__ import HELP_COMMANDS, HELP_COMMANDU, HELP_COMMANDA, HELP_COMMANDO, HELP_COMMANDAST
   cid=cbq.id
   cdt=cbq.data
   if cdt == "_admin_h":
      keyboard = InlineKeyboardMarkup(
            paginate_modules(0, HELP_COMMANDA, "help"))
      await cbq.edit_message_caption(
                            caption=f"This is the help for admin commmands to manage your group efficiently+{HELP_COMMANDA}",
                            reply_markup = keyboard)
   if cdt == "_util_h":
      keyboard = InlineKeyboardMarkup([
            paginate_modules(0, HELP_COMMANDU, "help"),
            
               [InlineKeyboardButton(
                            "Back",
                            callback_data= "b_k"
             )],
               [InlineKeyboardButton(
                            "Close",
                            callback_data= "kloz"
             )],
        ])
      await cbq.edit_message_caption(
                            caption="This is the help for util commmands to make your life easy peasy",
                            reply_markup = keyboard)
   if cdt == "_ast_h":
      keyboard = InlineKeyboardMarkup([
            paginate_modules(0, HELP_COMMANDAST, "help"),
               [InlineKeyboardButton(
                            "Back",
                            callback_data= "b_k"
             )],
               [InlineKeyboardButton(
                            "Close",
                            callback_data= "kloz"
             )],
        ])
      await cbq.edit_message_caption(
                            caption="This is the help for assistant commmands to manage your userbot",
                            reply_markup = keyboard)
   if cdt == "_own_h":
      keyboard = InlineKeyboardMarkup([
            paginate_modules(0, HELP_COMMANDO, "help"),
               [InlineKeyboardButton(
                            "Back",
                            callback_data= "b_k"
             )],
               [InlineKeyboardButton(
                            "Close",
                            callback_data= "kloz"
             )],
        ])
      await cbq.edit_message_caption(
                            caption="This is the help for owner commmands ",
                            reply_markup = keyboard)
   if cdt == "b_k":
        keboard= InlineKeyboardMarkup(
                    [
                        [InlineKeyboardButton(
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
                            "Back",
                            callback_data= "b_k"
                  )]])
        await cbq.edit_message_caption(
                            caption=f"You are accessing help for **King Userbot** \n __Everyone is a king. Until the real king arrives.__",
                            reply_markup = keyboard)
   if cdt == "kloz":
         await cbq.message.delete()

async def help_button_callback(_, __, query):
    if re.match(r"help_", query.data):
        return True


help_button_create = filters.create(help_button_callback)
@setbot.on_callback_query(help_button_create)
async def help_button(_, query):    
    from kingbot.__main__ import HELP_COMMANDS, HELP_COMMANDU, HELP_COMMANDA, HELP_COMMANDO, HELP_COMMANDAST
    mod_match = re.match(r"help_module\((.+?)\)", query.data)
    back_match = re.match(r"help_back", query.data)
    if mod_match:
        module = mod_match.group(1)
        text = (
            "This is help for the plugins **{}**:\n".format(
                HELP_COMMANDS[module].__MODULE__
            )
            + HELP_COMMANDS[module].__HELP__
        )

        await query.message.edit(
            text=text,
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(
                            text="Back",
                            callback_data="help_back"
                        )
                    ]
                ]
            ),
        )

    elif back_match:
        await query.message.edit(
            text=("help_str").format(", ".join(COMMAND_PREFIXES)),
            reply_markup=InlineKeyboardMarkup(
                paginate_modules(0, HELP_COMMANDS, "help")
            ),
        )
    await query.answer()
