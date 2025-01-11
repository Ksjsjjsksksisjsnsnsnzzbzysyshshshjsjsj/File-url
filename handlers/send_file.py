import asyncio
import requests
import string
import random
from configs import Config
from pyrogram import Client
from pyrogram.types import Message
from pyrogram.errors import FloodWait
from handlers.helpers import str_to_b64

async def reply_forward(message: Message, file_id: int):
    try:
        await message.reply_text(
            f"Files will be deleted in 30 minutes to avoid copyright issues. Please forward and save them.",
            disable_web_page_preview=True,
            quote=True
        )
    except FloodWait as e:
        await asyncio.sleep(e.x)
        await reply_forward(message, file_id)


async def media_forward(bot: Client, user_id: int, file_id: int):
    try:
        if Config.FORWARD_AS_COPY:
            return await bot.copy_message(chat_id=user_id, from_chat_id=Config.DB_CHANNEL, message_id=file_id)
        else:
            return await bot.forward_messages(chat_id=user_id, from_chat_id=Config.DB_CHANNEL, message_ids=file_id)
    except FloodWait as e:
        await asyncio.sleep(e.value)
        return await media_forward(bot, user_id, file_id)

async def send_media_and_reply(bot: Client, user_id: int, file_ids):
    """
    Forward all files in file_ids (list or single file_id) to the user.
    Send a single notification message after all media are forwarded.
    """
    # Ensure file_ids is a list
    if not isinstance(file_ids, list):
        file_ids = [file_ids]

    # Forward all files one by one
    sent_messages = []
    for file_id in file_ids:
        sent_message = await media_forward(bot, user_id, file_id)
        sent_messages.append(sent_message)

    # Send a single notification after all media are forwarded
    notification_msg = await bot.send_message(
        chat_id=user_id,
        text="<b>‼️Forward the Files to Saved Messages or somewhere else before Downloading it.</b>\n<b>It will get Deleted after 30 minutes.‼️</b>",
        parse_mode=ParseMode.HTML
    )

    # Schedule deletion for all messages (including the notification) after 30 minutes
    for message in sent_messages:
        asyncio.create_task(delete_after_delay(message, 1800))
    asyncio.create_task(delete_after_delay(notification_msg, 1800))