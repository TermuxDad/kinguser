
import asyncio
import importlib
import sys
import time
import traceback

from pyrogram import idle
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton , InlineQuery ,Message, CallbackQuery, InlineQueryResultPhoto
from pyrogram import filters 
# import kingbot
from kingbot import setbot , get_bot , get_self 
from assistant import ALL_AST
from adminss import ALL_ADMINN
from utilss import ALL_UTILS
from ownerr import ALL_OWN
from uti.misc import paginate_modules


BOT_RUNTIME = 0
loop = asyncio.get_event_loop()
HNDLR="."

async def get_runtime():
    return BOT_RUNTIME

@kingbot.on_message(filters.command(start,HNDLR) & filters.user(AdminSettings))
async def h_lp(_ , message):
  BotUN= setbot.get_me().username
  res= kingbot.get_inline_bot_results(BotUN, "hlpin")
  await kingbot.send_inline_bot_result(message.chat.id, res.query_id, res.results[0].id)

@setbot.on_inline_query(filters.regex("hlpin"))
async def in_h_lp(_ , inlinequery):
  keboard= InlineKeyboardMarkup(
                    [
                        [InlineKeyboardButton(
                            "Group Admin Plugins",
                            callback_data= "_admin_h"
                        )]
                    ],
                    [
                        [InlineKeyboardButton(
                            "Util Plugins",
                            callback_data= "_util_h"
                        )],
                        [InlineKeyboardButton(
                            "ASSISTANT Plugins",
                            callback_data= "_ast_h"
                        )]
                    ],
                    [
                        [InlineKeyboardButton(
                            "OWNER Plugins",
                            callback_data= "_own_h"
                        )]
                    ],
                    [
                        [InlineKeyboardButton(
                            "Close the menu",
                            callback_data= "kloz"
                  )]])
  inline_query.answer(
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
@cowner
@setbot.on_callback_query(filters.user(AdminSettings))
async def cbire(_ , cbq: CallbackQuery):
   cid=cbq.id
   cdt=cbq.data
   if cdt == "_admin_h":
      keyboard = InlineKeyboardMarkup(
            paginate_modules(0, HELP_COMMANDA, "help"),
            [
               [InlineKeyboardButton(
                            "Back",
                            callback_data= "b_k"
             )]],
             [
               [InlineKeyboardButton(
                            "Close",
                            callback_data= "kloz"
             )]],
        )
      cbq.edit_message_caption(
                            caption="This is the help for admin commmands to manage your group efficiently",
                            reply_markup = keyboard)
   if cdt == "_util_h":
      keyboard = InlineKeyboardMarkup(
            paginate_modules(0, HELP_COMMANDU, "help"),
            [
               [InlineKeyboardButton(
                            "Back",
                            callback_data= "b_k"
             )]],
             [
               [InlineKeyboardButton(
                            "Close",
                            callback_data= "kloz"
             )]],
        )
      cbq.edit_message_caption(
                            caption="This is the help for util commmands to make your life easy peasy",
                            reply_markup = keyboard)
   if cdt == "_ast_h":
      keyboard = InlineKeyboardMarkup(
            paginate_modules(0, HELP_COMMANDAST, "help"),
            [
               [InlineKeyboardButton(
                            "Back",
                            callback_data= "b_k"
             )]],
             [
               [InlineKeyboardButton(
                            "Close",
                            callback_data= "kloz"
             )]],
        )
      cbq.edit_message_caption(
                            caption="This is the help for assistant commmands to manage your userbot",
                            reply_markup = keyboard)
   if cdt == "_own_h":
      keyboard = InlineKeyboardMarkup(
            paginate_modules(0, HELP_COMMANDO, "help"),
            [
               [InlineKeyboardButton(
                            "Back",
                            callback_data= "b_k"
             )]],
             [
               [InlineKeyboardButton(
                            "Close",
                            callback_data= "kloz"
             )]],
        )
      cbq.edit_message_caption(
                            caption="This is the help for owner commmands ",
                            reply_markup = keyboard)
   if cdt == "b_k":
        keboard= InlineKeyboardMarkup(
                    [
                        [InlineKeyboardButton(
                            "Group Admin Plugins",
                            callback_data= "_admin_h"
                        )]
                    ],
                    [
                        [InlineKeyboardButton(
                            "Util Plugins",
                            callback_data= "_util_h"
                        )],
                        [InlineKeyboardButton(
                            "ASSISTANT Plugins",
                            callback_data= "_ast_h"
                        )]
                    ],
                    [
                        [InlineKeyboardButton(
                            "OWNER Plugins",
                            callback_data= "_own_h"
                        )]
                    ],
                    [
                        [InlineKeyboardButton(
                            "Back",
                            callback_data= "b_k"
                  )]])
        cbq.edit_message_caption(
                            caption=f"You are accessing help for **King Userbot** \n __Everyone is a king. Until the real king arrives.__",
                            reply_markup = keyboard)
   if cdt == "kloz":
         cbq.message.delete()

async def reload_userbot():
    await kingbot.start()
    for modul in ALL_MODULES:
        imported_module = importlib.import_module("utilss." + modul)
        imported_module = importlib.import_module("ownerr." + modul)
        imported_module = importlib.import_module("adminss." + modul)
        importlib.reload(imported_module)

async def help_button_callback(_, __, query):
    if re.match(r"help_", query.data):
        return True


help_button_create = filters.create(help_button_callback)
@setbot.on_callback_query(help_button_create)
async def help_button(_, query):
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
async def reinitial_restart():
    await get_bot()
    await get_self()


async def reboot():
    global BOT_RUNTIME, HELP_COMMANDS
    importlib.reload(importlib.import_module("adminss"))
    importlib.reload(importlib.import_module("ownerr"))
    importlib.reload(importlib.import_module("utilss"))
    importlib.reload(importlib.import_module("assistant"))
    # await setbot.send_message(Owner, "Bot is restarting...")
    await setbot.restart()
    await kingbot.restart()
    await reinitial_restart()
    # Reset global var
    BOT_RUNTIME = 0
    HELP_COMMANDU = {}
    HELP_COMMANDA = {}
    HELP_COMMANDO = {}
    HELP_COMMANDAST = {}
    # Assistant bot
    
    for modul in ALL_UTILS:
        imported_module = importlib.import_module("utilss." + modul)
        if hasattr(imported_module, "__MODULE__") and imported_module.__MODULE__:
            imported_module.__MODULE__ = imported_module.__MODULE__
        if hasattr(imported_module, "__MODULE__") and imported_module.__MODULE__:
            if not imported_module.__MODULE__.lower() in HELP_COMMANDU:
                HELP_COMMANDU[imported_module.__MODULE__.lower()] = imported_module
            else:
                raise Exception("Can't have two modules with the same name! Please change one")
        if hasattr(imported_module, "__HELP__") and imported_module.__HELP__:
            HELP_COMMANDU[imported_module.__MODULE__.lower()] = imported_module
        importlib.reload(imported_module)
    for modula in ALL_ADMINN:
        imported_module = importlib.import_module("adminss." + modula)
        if hasattr(imported_module, "__MODULE__") and imported_module.__MODULE__:
            imported_module.__MODULE__ = imported_module.__MODULE__
        if hasattr(imported_module, "__MODULE__") and imported_module.__MODULE__:
            if not imported_module.__MODULE__.lower() in HELP_COMMANDA:
                HELP_COMMANDA[imported_module.__MODULE__.lower()] = imported_module
            else:
                raise Exception("Can't have two modules with the same name! Please change one")
        if hasattr(imported_module, "__HELP__") and imported_module.__HELP__:
            HELP_COMMANDA[imported_module.__MODULE__.lower()] = imported_module
        importlib.reload(imported_module)
    for modulst in ALL_OWN:
        imported_module = importlib.import_module("ownerr." + modulst)
        if hasattr(imported_module, "__MODULE__") and imported_module.__MODULE__:
            imported_module.__MODULE__ = imported_module.__MODULE__
        if hasattr(imported_module, "__MODULE__") and imported_module.__MODULE__:
            if not imported_module.__MODULE__.lower() in HELP_COMMANDO:
                HELP_COMMANDO[imported_module.__MODULE__.lower()] = imported_module
            else:
                raise Exception("Can't have two modules with the same name! Please change one")
        if hasattr(imported_module, "__HELP__") and imported_module.__HELP__:
            HELP_COMMANDO[imported_module.__MODULE__.lower()] = imported_module
        importlib.reload(imported_module)
    for modula in ALL_AST:
            imported_module = importlib.import_module("assistant." + modul)
            if hasattr(imported_module, "__MODULE__") and imported_module.__MODULE__:
                imported_module.__MODULE__ = imported_module.__MODULE__
            if hasattr(imported_module, "__MODULE__") and imported_module.__MODULE__:
                if not imported_module.__MODULE__.lower() in HELP_COMMANDAST:
                    HELP_COMMANDAST[imported_module.__MODULE__.lower()] = imported_module
                else:
                    raise Exception("Can't have two modules with the same name! Please change one")
            if hasattr(imported_module, "__HELP__") and imported_module.__HELP__:
                HELP_COMMANDAST[imported_module.__MODULE__.lower()] = imported_module
            importlib.reload(imported_module)
    HELP_COMMANDS = {**HELP_COMMANDA,**HELP_COMMANDU,**HELP_COMMANDO, **HELP_COMMANDAST}

# await setbot.send_message(Owner, "Restart successfully!")

async def restart_all():
    # Restarting and load all plugins
    asyncio.get_event_loop().create_task(reboot())


RANDOM_STICKERS = ["CAADAgAD6EoAAuCjggf4LTFlHEcvNAI", "CAADAgADf1AAAuCjggfqE-GQnopqyAI",
                   "CAADAgADaV0AAuCjggfi51NV8GUiRwI"]


async def except_hook(errtype, value, tback):
    sys.__excepthook__(errtype, value, tback)
    errors = traceback.format_exception(etype=errtype, value=value, tb=tback)
    button = InlineKeyboardMarkup([[InlineKeyboardButton("🐞 Report bugs", callback_data="report_errors")]])
    text = "An error has accured!\n\n```{}```\n".format("".join(errors))
    if errtype == ModuleNotFoundError:
        text += "\nHint: Try this in your terminal `pip install -r requirements.txt`"
    await setbot.send_message(Owner, text, reply_markup=button)


async def reinitial():
    await kingbot.start()
    await setbot.start()
    await get_self()
    await get_bot()
    await kingbot.stop()
    await setbot.stop()


async def start_bot():
    # sys.excepthook = except_hook
    print("----- Checking user and bot... -----")
    await reinitial()
    print("----------- Check done! ------------")
    # Assistant bot
    await setbot.start()
    await kingbot.start()
    
    for modul in ALL_UTILS:
        imported_module = importlib.import_module("utilss." + modul)
        if hasattr(imported_module, "__MODULE__") and imported_module.__MODULE__:
            imported_module.__MODULE__ = imported_module.__MODULE__
        if hasattr(imported_module, "__MODULE__") and imported_module.__MODULE__:
            if not imported_module.__MODULE__.lower() in HELP_COMMANDU:
                HELP_COMMANDU[imported_module.__MODULE__.lower()] = imported_module
            else:
                raise Exception("Can't have two modules with the same name! Please change one")
        if hasattr(imported_module, "__HELP__") and imported_module.__HELP__:
            HELP_COMMANDU[imported_module.__MODULE__.lower()] = imported_module
    for modula in ALL_ADMINN:
        imported_module = importlib.import_module("adminss." + modula)
        if hasattr(imported_module, "__MODULE__") and imported_module.__MODULE__:
            imported_module.__MODULE__ = imported_module.__MODULE__
        if hasattr(imported_module, "__MODULE__") and imported_module.__MODULE__:
            if not imported_module.__MODULE__.lower() in HELP_COMMANDA:
                HELP_COMMANDA[imported_module.__MODULE__.lower()] = imported_module
            else:
                raise Exception("Can't have two modules with the same name! Please change one")
        if hasattr(imported_module, "__HELP__") and imported_module.__HELP__:
            HELP_COMMANDA[imported_module.__MODULE__.lower()] = imported_module
    for modulst in ALL_OWN:
        imported_module = importlib.import_module("ownerr." + modulst)
        if hasattr(imported_module, "__MODULE__") and imported_module.__MODULE__:
            imported_module.__MODULE__ = imported_module.__MODULE__
        if hasattr(imported_module, "__MODULE__") and imported_module.__MODULE__:
            if not imported_module.__MODULE__.lower() in HELP_COMMANDO:
                HELP_COMMANDO[imported_module.__MODULE__.lower()] = imported_module
            else:
                raise Exception("Can't have two modules with the same name! Please change one")
        if hasattr(imported_module, "__HELP__") and imported_module.__HELP__:
            HELP_COMMANDO[imported_module.__MODULE__.lower()] = imported_module
    for modula in ALL_AST:
            imported_module = importlib.import_module("assistant." + modul)
            if hasattr(imported_module, "__MODULE__") and imported_module.__MODULE__:
                imported_module.__MODULE__ = imported_module.__MODULE__
            if hasattr(imported_module, "__MODULE__") and imported_module.__MODULE__:
                if not imported_module.__MODULE__.lower() in HELP_COMMANDAST:
                    HELP_COMMANDAST[imported_module.__MODULE__.lower()] = imported_module
                else:
                    raise Exception("Can't have two modules with the same name! Please change one")
            if hasattr(imported_module, "__HELP__") and imported_module.__HELP__:
                HELP_COMMANDAST[imported_module.__MODULE__.lower()] = imported_module
            await idle()
    HELP_COMMANDS = {**HELP_COMMANDA,**HELP_COMMANDU,**HELP_COMMANDO, **HELP_COMMANDAST}

Owner= get_self().Owner
if __name__ == '__main__':
    BOT_RUNTIME = int(time.time())
    loop.run_until_complete(start_bot())
