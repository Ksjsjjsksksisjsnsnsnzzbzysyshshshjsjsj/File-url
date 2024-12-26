import asyncio
import requests
import string
import random
from configs import Config
from pyrogram import Client
from pyrogram.errors import FloodWait
from handlers.helpers import str_to_b64

async def notify_user(bot: Client, user_id: int):
    try:
        await bot.send_message(
            chat_id=user_id,
            text="Your files have been delivered and will be deleted in 30 minutes. Please save them promptly.",
            disable_web_page_preview=True
        )
    except FloodWait as e:
        await asyncio.sleep(e.x)
        await bot.send_message(
            chat_id=user_id,
            text="Your files have been delivered and will be deleted in 30 minutes. Please save them promptly.",
            disable_web_page_preview=True
        )

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

async def send_media_and_reply(bot: Client, user_id: int, file_id: int):
    sent_message = await media_forward(bot, user_id, file_id)
    asyncio.create_task(delete_after_delay(sent_message, 1800))

    # Send a separate notification to the user
    await notify_user(bot, user_id)

async def delete_after_delay(message, delay):
    await asyncio.sleep(delay)
    await message.delete()