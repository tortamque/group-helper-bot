from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def build_main_keyboard():
    item_queue = InlineKeyboardButton(text='Очереди', callback_data='queue')
    item_timetable = InlineKeyboardButton(text='Расписание', callback_data='timetable')
    item_db = InlineKeyboardButton(text='Управление базой данных', callback_data='db')
    item_admin = InlineKeyboardButton(text='Инструменты', callback_data='tools')
    keyboard_main = InlineKeyboardMarkup([[item_queue], [item_timetable], [item_db], [item_admin]])

    return keyboard_main


def generate_calback_query_template(text: str, callback_query):
    keyboard = build_main_keyboard()
    callback_query.edit_message_text(text, reply_markup=keyboard)


def answer_main(callback_query):
    text = '<b>Помощь</b>\n\n👇 Нажми на кпонки внизу, что бы получить дополнительную информацию.'
    generate_calback_query_template(text, callback_query)
