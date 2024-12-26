import asyncio
import requests
import string
import random
from configs import Config
from pyrogram import Client
from pyrogram.types import Message
from pyrogram.errors import FloodWait
from handlers.helpers import str_to_b64


async def media_forward(bot: Client, user_id: int, file_id: int):
    try:
        if Config.FORWARD_AS_COPY is True:
            return await bot.copy_message(chat_id=user_id, from_chat_id=Config.DB_CHANNEL,
                                          message_id=file_id)
        elif Config.FORWARD_AS_COPY is False:
            return await bot.forward_messages(chat_id=user_id, from_chat_id=Config.DB_CHANNEL,
                                              message_ids=file_id)
    except FloodWait as e:
        await asyncio.sleep(e.value)
        return await media_forward(bot, user_id, file_id)

async def send_media_and_reply(bot: Client, user_id: int, file_ids):
    # Ensure file_ids is always a list
    if isinstance(file_ids, int):  # If a single file ID is provided
        file_ids = [file_ids]

    # Forward all media files to the user
    sent_messages = []
    for file_id in file_ids:
        sent_message = await media_forward(bot, user_id, file_id)
        sent_messages.append(sent_message)
        # Schedule deletion for each forwarded message
        asyncio.create_task(delete_after_delay(sent_message, 1800))
    
    # Send a single wait message after all files are forwarded
    try:
        await bot.send_message(
            chat_id=user_id,
            text="Thank you for waiting! Your files are ready and will be deleted in 30 minutes.",
            disable_web_page_preview=True
        )
    except FloodWait as e:
        await asyncio.sleep(e.x)
        await bot.send_message(
            chat_id=user_id,
            text="Thank you for waiting! Your files are ready and will be deleted in 30 minutes.",
            disable_web_page_preview=True
        )

async def delete_after_delay(message, delay):
    await asyncio.sleep(delay)
    await message.delete()