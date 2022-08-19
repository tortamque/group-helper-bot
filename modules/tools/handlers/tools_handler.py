from pyrogram import filters

from config.config import chat_id as working_chat_id, bot_username
from config.app import app


@app.on_message(filters.group & filters.command(["ping", f"ping@{bot_username}"]) & filters.chat([working_chat_id]))
def ping(client, message):
    message.reply_text("Pong")


@app.on_message(filters.group & filters.command(["chat_id", f"chat_id@{bot_username}"]))
def chat_id(client, message):
    chatid = message.chat.id

    message.reply_text(text=f"<code>{chatid}</code>")


@app.on_message(filters.group & filters.command(["user_id", f"user_id@{bot_username}"]))
def user_id(client, message):
    if message.reply_to_message:
        userid = message.reply_to_message.from_user.id
    else:
        userid = message.from_user.id

    message.reply_text(text=f"<code>{userid}</code>")


@app.on_message(filters.group & ~filters.chat([working_chat_id]))
def not_allowed_chat(client, message):
    message.reply_text(text="Я отказываюсь работать в этом чате.")


@app.on_message(filters.private)
def private(client, message):
    message.reply_text(text="Я не работаю в личных сообщениях.")

