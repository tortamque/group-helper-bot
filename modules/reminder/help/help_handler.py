from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def build_main_keyboard():
    item_setup_db = InlineKeyboardButton(text='Настроить бд', callback_data='setup_db')
    item_show_db = InlineKeyboardButton(text='Показать содержимое бд', callback_data='show_db')
    item_reset_db = InlineKeyboardButton(text='Очистить бд', callback_data='reset_db')
    item_editlink = InlineKeyboardButton(text='Изменить ссылку на пару', callback_data='editlink')
    item_ids = InlineKeyboardButton(text='Получить ID пар', callback_data='ids')
    back_button = InlineKeyboardButton(text='Назад', callback_data='main')
    keyboard = InlineKeyboardMarkup([[item_setup_db, item_reset_db], [item_show_db, item_editlink], [item_ids], [back_button]])

    return keyboard


def get_db_keyboard_template():
    back_button = InlineKeyboardButton(text='Назад', callback_data='db')
    keyboard = InlineKeyboardMarkup([[back_button]])

    return keyboard


def generate_calback_query_template(text: str, callback_query):
    keyboard = get_db_keyboard_template()
    callback_query.edit_message_text(text, reply_markup=keyboard)


def answer_db(client, callback_query):
    if callback_query.data == 'db':
        keyboard = build_main_keyboard()
        callback_query.edit_message_text('<b>Управление базой данных</b>\n\n👇 Нажимай на кнопки внизу, что бы получить дополнительную информацию.',reply_markup=keyboard)
    elif callback_query.data == 'setup_db':
        text = '<b>Настроить бд</b>\n❗️ Только для админа\n\nИспользование:\n<code>/setup_db</code>'
        generate_calback_query_template(text, callback_query)
    elif callback_query.data == 'show_db':
        text = '<b>Показать содержимое бд</b>\n❗️ Только для админа\n\nИспользование:\n<code>/show_db</code>'
        generate_calback_query_template(text, callback_query)
    elif callback_query.data == 'reset_db':
        text = '<b>Очистить бд</b>\n❗️ Только для админа\n\nИспользование:\n<code>/reset_db</code>'
        generate_calback_query_template(text, callback_query)
    elif callback_query.data == 'editlink':
        text = '<b>Изменить ссылку на пару в БД</b>\n❗️ Только для админа\n\nИспользование:\n<code>/editlink <Айди пары> <Новая ссылка></code>'
        generate_calback_query_template(text, callback_query)
    elif callback_query.data == 'ids':
        text = '<b>Получить ID пар</b>\n❗️ Только для админа\n\nИспользование:\n<code>/ids</code>'
        generate_calback_query_template(text, callback_query)
