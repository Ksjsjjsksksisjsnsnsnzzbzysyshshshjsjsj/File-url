import os

p = os.environ.get("CRAZY_PARMANANT_URL", "https://telegramfilestorebot.blogspot.com/2024/12/test.html")
class Config(object):
  API_ID = int(os.environ.get("API_ID", "29534418"))
  API_HASH = os.environ.get("API_HASH", "5f15dd792990ade40a43ae17413b422f")
  BOT_TOKEN = os.environ.get("BOT_TOKEN", "8073834357:AAG0AcIdc5rkA9k1bHPJ1XR4zdZKsb24S7g")
  BOT_USERNAME = os.environ.get("BOT_USERNAME", "Testsstoreeee_bot")
  DB_CHANNEL = int(os.environ.get("DB_CHANNEL", "-1002422010138"))
  SHORTLINK_URL = os.environ.get('SHORTLINK_URL', "tryshort.in")
  SHORTLINK_API = os.environ.get('SHORTLINK_API', "71f721dc31c2c4e0731da9e7e116255b4df7b67c")
  BOT_OWNER = int(os.environ.get("BOT_OWNER", "5691486059"))
  SECONDS = int(os.environ.get("SECONDS", "1800"))
  DATABASE_URL = os.environ.get("DATABASE_URL", "mongodb+srv://ks0360683:Ybz9rKOKYilsb38w@cluster0.x6nn0.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
  UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL", "")
  LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1002240620811"))
  BANNED_USERS = set(int(x) for x in os.environ.get("BANNED_USERS", "").split())
  FORWARD_AS_COPY = bool(os.environ.get("FORWARD_AS_COPY", True))
  BROADCAST_AS_COPY = bool(os.environ.get("BROADCAST_AS_COPY", True))
  BANNED_CHAT_IDS = list(set(int(x) for x in os.environ.get("BANNED_CHAT_IDS", "").split()))
  OTHER_USERS_CAN_SAVE_FILE = bool(os.environ.get("OTHER_USERS_CAN_SAVE_FILE", False))
  ABOUT_BOT_TEXT = f"""
This is a Permanent FileStore Bot. 
Send Me any Media or File. I can Work In Channel too. Add Me to Channel with Edit Permission, I will add save Uploaded File in Channel and Share a Shareable Link. 

╭────[ 🔅FɪʟᴇSᴛᴏʀᴇBᴏᴛ🔅]────⍟
│
├🔸 My Name: [FileStore Bot](https://t.me/{BOT_USERNAME})
│
├🔸 Language: [Python 3](https://www.python.org)
│
├🔹 Library: [Pyrogram](https://docs.pyrogram.org)
│
╰──────[ 😎 ]───────────⍟
"""
  ABOUT_DEV_TEXT = f"""
🧑🏻‍💻 𝗗𝗲𝘃𝗲𝗹𝗼𝗽𝗲𝗿: [lt](https://telegram.me/)
 
 I am Super noob Please Support My Hard Work.

[Donate Me](https://t.me/)
"""
  HOME_TEXT = """
Hello,This is a Permanent FileStore Bot .
"""
