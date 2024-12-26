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
        return media_forward(bot, user_id, file_id)

async def send_media_and_reply(bot: Client, user_id: int, file_id: int):
    # Forward media to the user
    sent_message = await media_forward(bot, user_id, file_id)
    
    
    
    # Schedule deletion after a delay
    asyncio.create_task(delete_after_delay(sent_message, 1800))
    
    # Send a wait message
    try:
        await message.reply_text(
            "Thank you for waiting! Your file is ready and will be deleted in 30 minutes.",
            disable_web_page_preview=True,
            quote=True
        )
    except FloodWait as e:
        await asyncio.sleep(e.x)
        await message.reply_text(
            "Thank you for waiting! Your file is ready and will be deleted in 30 minutes.",
            disable_web_page_preview=True,
            quote=True
        )

async def delete_after_delay(message, delay):
    await asyncio.sleep(delay)
    await message.delete()