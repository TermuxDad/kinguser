import pytgcalls
import os
from datetime import datetime
from distutils.util import strtobool as sb
from logging import DEBUG, INFO, basicConfig, getLogger
from logging import warning as wr
from pyrogram import Client
from decouple import config
from uti.confi import Var
LOGS = getLogger(__name__)

if not Var.API_ID or not Var.API_HASH:
    wr("No API_ID or API_HASH found.    Quiting...")
    exit(1)




START_TIME = datetime.now()

try:
    if Var.HANDELR:
        HNDLR = Var.HANDELR
    else:
        HNDLR = "."
    if not Var.SUDO
        SUDO = None
    else
        SUDO =Var.Sudo
except BaseException:
    pass



if Var.VC_SESSION
    try:
        client = Client(Var.VC_SESSSION, Var.VC_API_ID, Var.VC_API_HASH)
        vcbot = PyTgCalls(client)
else:
    vcbot = None

# Postgresqlw5mj by
def mulaisql() -> scoped_session:
    global DB_AVAILABLE
    engine = create_engine(Var.DB_URI, client_encoding="utf8")
    BASE.metadata.bind = engine
    try:
        BASE.metadata.create_all(engine)
    except exc.OperationalError:
        DB_AVAILABLE = False
        return False
    DB_AVAILABLE = True
    return scoped_session(sessionmaker(bind=engine, autoflush=False))


async def get_bot_inline(bot):
    global BOTINLINE_AVAIABLE
    if setbot:
        try:
            await naruto.get_inline_bot_results("@{}".format(bot.username), "test")
            BOTINLINE_AVAIABLE = True
        except errors.exceptions.bad_request_400.BotInlineDisabled:
            BOTINLINE_AVAIABLE = False


async def get_self():
    global Owner, OwnerName, OwnerUsername, AdminSettings
    getself = await naruto.get_me()
    Owner = getself.id
    if getself.last_name:
        OwnerName = getself.first_name + " " + getself.last_name
    else:
        OwnerName = getself.first_name
    OwnerUsername = getself.username
    if Owner not in AdminSettings:
        AdminSettings.append(Owner)


async def get_bot():
    global BotID, BotName, BotUsername
    getbot = await setbot.get_me()
    BotID = getbot.id
    BotName = getbot.first_name
    BotUsername = getbot.username
BotUN= BotUsername

BASE = declarative_base()
SESSION = mulaisql()
setbot = Client(":memory:",api_id=Var.API_ID, api_hash=Var.API_HASH, bot_token=Var.BOT_TOKEN )
naruto = Client(Var.SESSION, api_id=Var.API_ID, api_hash=Var.API_HASH)
async def edrep(msg: Message, **kwargs):
    func = msg.edit_text if msg.from_user.is_self else msg.reply
    spec = getfullargspec(func.__wrapped__).args
    await func(**{k: v for k, v in kwargs.items() if k in spec})
