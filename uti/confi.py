from decouple import config
from dotenv import find_dotenv, load_dotenv

load_dotenv(find_dotenv())


class Var(object):
    # Mandatory
    API_ID = config("API_ID", default=None, cast=int)
    API_HASH = config("API_HASH", default=None)
    BOT_TOKEN = config("BOT_TOKEN", default=None)
    BOT_USERNAME = config("BOT_USERNAME", default=None)
    SESSION = config("SESSION", default=None)
    DB_URI = config("DATABASE_URL", default=None)
    LOG_CHANNEL = config("LOG_CHANNEL", default=None, cast=int)
    BLACKLIST_CHAT = set(int(x) for x in config("BLACKLIST_CHAT", "").split())
    try:
        OWNER_ID = config("OWNER_ID", default=None, cast=int)
    except BaseException:
        pass
    # heroku stuff
    try:
        HEROKU_APP_NAME = config("HEROKU_APP_NAME", default=None)
        HEROKU_API = config("HEROKU_API", default=None)
    except BaseException:
        HEROKU_APP_NAME = None
        HEROKU_API = None
    
    try:
        VC_SESSSION = config("VC_SESSSION", default=None)
        VC_API_ID = config("VC_API_ID", default=None)
        VC_API_HASH = config("VC_API_HASH", default=None)
        HANDLER = config("COMMAND_HANDLER", default=None)
        SUDO = set(int(x) for x in config("SUDO_USERS", "").split())
    except BaseException:
        VC_SESSSION= None
        VC_API_ID = None
        VC_API_HASH= None
        HANDLER= None
        SUDO= None