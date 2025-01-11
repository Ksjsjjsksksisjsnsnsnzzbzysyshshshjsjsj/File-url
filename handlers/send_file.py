import asyncio
import requests
import string
import random
from configs import Config
from pyrogram import Client
from pyrogram.enums import ParseMode, ChatAction
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
        if Config.FORWARD_AS_COPY is True:
            return await bot.copy_message(chat_id=user_id, from_chat_id=Config.DB_CHANNEL,
                                          message_id=file_id)
        elif Config.FORWARD_AS_COPY is False:
            return await bot.forward_messages(chat_id=user_id, from_chat_id=Config.DB_CHANNEL,
                                              message_ids=file_id)
    except FloodWait as e:
        await asyncio.sleep(e.value)
        return media_forward(bot, user_id, file_id)
        await message.delete()


async def send_media_and_reply(bot: Client, user_id: int, file_id: int):
    # Forward the media to the user
    sent_message = await media_forward(bot, user_id, file_id)

    # Send a notification message
    notification_msg = await bot.send_message(
        chat_id=user_id,
        text="<b>‼️Forward the Files to Saved Messages or somewhere else before Downloading it.</b>\n<b>It will get Deleted after 30 minutes.‼️</b>",
        parse_mode=ParseMode.HTML
    )

    # Schedule deletion after 30 minutes (1800 seconds)
    asyncio.create_task(delete_after_delay(sent_message, notification_msg, 1800))

async def delete_after_delay(sent_message, notification_msg, delay):
    # Wait for the specified delay
    await asyncio.sleep(delay)

    # Delete the sent message and notification
    await sent_message.delete()
    await notification_msg.delete()