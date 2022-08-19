from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def build_main_keyboard():
    item_create = InlineKeyboardButton(text='Создать очередь', callback_data='create')
    item_delete = InlineKeyboardButton(text='Удалить очередь', callback_data='delete')
    item_join = InlineKeyboardButton(text='Записаться в очередь', callback_data='join')
    item_leave = InlineKeyboardButton(text='Выйти из очереди', callback_data='leave')
    item_check = InlineKeyboardButton(text='Проверить очередь', callback_data='check')
    item_reset = InlineKeyboardButton(text='Удалить все очередли', callback_data='reset')
    item_pass = InlineKeyboardButton(text='Пропустить человека', callback_data='pass')
    back_button = InlineKeyboardButton(text='Назад', callback_data='main')
    keyboard_main = InlineKeyboardMarkup([[item_create, item_delete], [item_join, item_leave], [item_check, item_pass], [item_reset], [back_button]])

    return keyboard_main


def get_queue_keyboard_template():
    back_button = InlineKeyboardButton(text='Назад', callback_data='queue')
    keyboard = InlineKeyboardMarkup([[back_button]])

    return keyboard


def generate_callback_query_template(text: str, callback_query):
    keyboard = get_queue_keyboard_template()
    callback_query.edit_message_text(text, reply_markup=keyboard)


def answer_queue(client, callback_query):
    if callback_query.data == 'queue':
        keyboard_main = build_main_keyboard()
        callback_query.edit_message_text(text='<b>Очереди</b>\n\n👇 Нажми на кпонки внизу, что бы получить дополнительную информацию.',reply_markup=keyboard_main)
    elif callback_query.data == 'create':
        text = '<b>Создание очереди</b>\n\nДля создания очереди используй команду\n<code>/create название</code>\nПример: <code>/create новая очередь</code>'
        generate_callback_query_template(text, callback_query)
    elif callback_query.data == 'delete':
        text = '<b>Удаление очереди</b>\n\nДля удаления очереди используй команду\n<code>/delete название</code>\nПример: <code>/delete ненужная очередь</code>\n\nУдалить очередь может только её создатель или администратор.'
        generate_callback_query_template(text, callback_query)
    elif callback_query.data == 'join':
        text = '<b>Запись в очередь</b>\n\nДля записи в очередь используй команду\n<code>/join название</code>\nПример: <code>/join название очереди</code>'
        generate_callback_query_template(text, callback_query)
    elif callback_query.data == 'leave':
        text = '<b>Выход из очереди</b>\n\nДля выхода из очереди используй команду\n<code>/leave название</code>\nПример: <code>/leave название очереди</code>'
        generate_callback_query_template(text, callback_query)
    elif callback_query.data == 'check':
        text = '<b>Проверка очереди</b>\n\nВыводит все существующие очереди и их учасников.\nПример:\n<code>/check</code>'
        generate_callback_query_template(text, callback_query)
    elif callback_query.data == 'pass':
        text = '<b>Пропустить людей в очереди</b>\n\nПропускает n людей после тебя.\nИспользование:\n<code>/pass <кол-во людей> <название очереди></code>'
        generate_callback_query_template(text, callback_query)
    elif callback_query.data == 'reset':
        text = '<b>Удалить все очереди</b>\n❗️ Только для админа\n\nУдаляет все очереди\nИспользование:\n<code>/reset</code>'
        generate_callback_query_template(text, callback_query)
