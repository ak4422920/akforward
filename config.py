from os import environ 

class Config:
    API_ID = int(environ.get("API_ID", "29171167"))
    API_HASH = environ.get("API_HASH", "7ea2149629e445936619f06a3c0dc716")
    BOT_TOKEN = environ.get("BOT_TOKEN", "") 
    BOT_SESSION = environ.get("BOT_SESSION", "AKautoforward_bot") 
    DATABASE_URI = environ.get("DATABASE_URI", "")
    DATABASE_NAME = environ.get("DATABASE_NAME", "")
    BOT_OWNER = int(environ.get("BOT_OWNER", "7251898668"))

class temp(object): 
    lock = {}
    CANCEL = {}
    forwardings = 0
    BANNED_USERS = []
    IS_FRWD_CHAT = []
