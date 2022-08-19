from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def build_main_keyboard():
    item_ping = InlineKeyboardButton(text='Пинг', callback_data='ping')
    item_chat_id = InlineKeyboardButton(text='Получить ID чата', callback_data='chat_id')
    item_user_id = InlineKeyboardButton(text='Получить ID пользователя', callback_data='user_id')
    back_button = InlineKeyboardButton(text='Назад', callback_data='main')
    keyboard = InlineKeyboardMarkup([[item_ping], [item_chat_id, item_user_id], [back_button]])

    return keyboard


def get_tools_keyboard_template():
    back_button = InlineKeyboardButton(text='Назад', callback_data='tools')
    keyboard = InlineKeyboardMarkup([[back_button]])

    return keyboard


def generate_callback_query_template(text: str, callback_query):
    keyboard = get_tools_keyboard_template()
    callback_query.edit_message_text(text, reply_markup=keyboard)


def answer_tools(client, callback_query):
    if callback_query.data == 'tools':
        keyboard = build_main_keyboard()
        callback_query.edit_message_text(text='<b>Административные команды</b>\n\n👇 Нажимай на кнопки внизу, что бы получить дополнительную информацию.',reply_markup=keyboard)
    elif callback_query.data == 'ping':
        text = '<b>Пинг</b>\n\nИспользование:\n<code>/ping</code>'
        generate_callback_query_template(text, callback_query)
    elif callback_query.data == 'chat_id':
        text = '<b>Получить ID чата</b>\n\nИспользование:\n<code>/chat_id</code>'
        generate_callback_query_template(text, callback_query)
    elif callback_query.data == 'user_id':
        text = '<b>Получить ID пользователя</b>\n\nИспользование:\n<code>/user_id</code> - покажет ID пользователя, который отправил эту команду\n<code>/user_id</code> в ответ на сообщение - покажет ID пользователя, на которого ответили'
        generate_callback_query_template(text, callback_query)
