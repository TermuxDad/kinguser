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
    DB_URI = config("DATABASE_URI", default=None)
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
    REDIS_URI = config("REDIS_URI", default=None)
    REDIS_PASSWORD = config("REDIS_PASSWORD", default=None)
