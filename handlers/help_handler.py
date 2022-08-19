from pyrogram import filters

from config.app import app
from config.config import chat_id, bot_username
from handlers.help.main_page_help_handler import build_main_keyboard


@app.on_message(filters.group & filters.command(["help", f"help@{bot_username}", "start", f"start@{bot_username}"]) & filters.chat([chat_id]))
def help_main(client, message):
    keyboard = build_main_keyboard()

    app.send_message(chat_id=message.chat.id, text='<b>Помощь</b>\n\n👇 Нажимай на кнопки внизу, что бы получить дополнительную информацию.', reply_markup=keyboard)
