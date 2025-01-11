import asyncio
from pyrogram import Client
from pyrogram.enums import ParseMode
from pyrogram.types import Message
from pyrogram.errors import FloodWait
from configs import Config

async def media_forward(bot: Client, user_id: int, file_id: int):
    try:
        if Config.FORWARD_AS_COPY is True:
            return await bot.copy_message(chat_id=user_id, from_chat_id=Config.DB_CHANNEL, message_id=file_id)
        else:
            return await bot.forward_messages(chat_id=user_id, from_chat_id=Config.DB_CHANNEL, message_ids=file_id)
    except FloodWait as e:
        await asyncio.sleep(e.value)
        return await media_forward(bot, user_id, file_id)

async def send_notification(bot: Client, user_id: int, delay: int = 1800):
    """
    Send a single notification message and return the message object.
    """
    notification_msg = await bot.send_message(
        chat_id=user_id,
        text=(
            "<b>‼️ Forward the Files to Saved Messages or somewhere else before Downloading it.</b>\n"
            "<b>It will get Deleted after 30 minutes.‼️</b>"
        ),
        parse_mode=ParseMode.HTML
    )
    return notification_msg


async def send_media_and_reply(bot: Client, user_id: int, file_id: int):
    # Forward the media to the user
    sent_message = await media_forward(bot, user_id, file_id)
    
    # Send a notification message and capture the message object
    notification_msg = await send_notification(bot, user_id)

    # Schedule deletion after 30 minutes (1800 seconds)
    asyncio.create_task(delete_after_delay(sent_message, notification_msg, 1800))


async def delete_after_delay(sent_message, notification_msg, delay):
    # Wait for the specified delay
    await asyncio.sleep(delay)

    # Delete the sent message and notification
    await sent_message.delete()
    await notification_msg.delete()