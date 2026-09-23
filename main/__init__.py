#Join me at telegram @dev_gagan

from pyrogram import Client

from telethon.sessions import StringSession
from telethon.sync import TelegramClient

from decouple import config
import logging, time, sys

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logging.getLogger("pyrogram").setLevel(logging.WARNING)
logging.getLogger("telethon").setLevel(logging.WARNING)


# variables
API_ID = config("25520653", default=None, cast=int)
API_HASH = config("5e99595580628982d3fdb6066657b8ca", default=None)
BOT_TOKEN = config("8980179743:AAE-zz5vNsvnw8tB641vNQdsbT1fsP9nn0k", default=None)
SESSION = config("BQHOJcMAqzzbQ3DEmWxqs8BHJJC_SkSqrivy42gaBLV3QXgNF4q_A-Y0Qy8Nhbyv7_Wu12y2lhUmYR7ssy-SM5YcT4JCld9JX87l5SqNyVJRT2Sxfaq1weLjwmodVwrQunnGazHH-B8ClSTG6DnBwQUCgqVQA0AAkylwJbdHRdVMC6J-t6k6xGBAd3DvpYDEme-4P9naGox2HVqxbID7gUyzTRxNSti21oDCh4xSmI0b9KaZHGriteMnAJyRsau2yN23VWOChrcr9iWQ5b2lmxfaaDATTCvgKZwpmo1KkGHYIXKWJQSGY_YU4CtAtVflxbN8fCpDoI4T6whSa5zkVfyknshNHgAAAAGMN7bJAA", default=None)
FORCESUB = config("-1003746021917", default=None)
AUTH = config("5825448865", default=None)
SUDO_USERS = []

if len(AUTH) != 0:
    SUDO_USERS = {int(AUTH.strip()) for AUTH in AUTH.split()}
else:
    SUDO_USERS = set()

bot = TelegramClient('bot', API_ID, API_HASH).start(bot_token=BOT_TOKEN) 

userbot = Client("myacc",api_id=API_ID,api_hash=API_HASH,session_string=SESSION)

try:
    userbot.start()
except BaseException:
    print("Your session expired please re add that... thanks @dev_gagan.")
    sys.exit(1)

Bot = Client(
    "SaveRestricted",
    bot_token=BOT_TOKEN,
    api_id=int(API_ID),
    api_hash=API_HASH
)    

try:
    Bot.start()
except Exception as e:
    #print(e)
    logger.info(e)
    sys.exit(1)
