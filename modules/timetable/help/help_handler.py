from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def build_main_keyboard():
    item_week = InlineKeyboardButton(text='Расписание на текущ. неделю', callback_data='timetable_week')
    item_nextweek = InlineKeyboardButton(text='Расписание на след. неделю', callback_data='timetable_nextweek')
    item_today = InlineKeyboardButton(text='Расписание на сегодня', callback_data='timetable_today')
    item_tomorrow = InlineKeyboardButton(text='Расписание на завтра', callback_data='timetable_tomorrow')
    back_button = InlineKeyboardButton(text='Назад', callback_data='main')
    keyboard = InlineKeyboardMarkup([[item_week], [item_nextweek], [item_today], [item_tomorrow], [back_button]])

    return keyboard


def get_timetable_keyboard_template():
    back_button = InlineKeyboardButton(text='Назад', callback_data='timetable')
    keyboard = InlineKeyboardMarkup([[back_button]])

    return keyboard


def generate_callback_query_template(text: str, callback_query):
    keyboard = get_timetable_keyboard_template()
    callback_query.edit_message_text(text, reply_markup=keyboard)


def answer_timetable(client, callback_query):
    if callback_query.data == 'timetable':
        keyboard = build_main_keyboard()
        callback_query.edit_message_text('<b>Расписание</b>', reply_markup=keyboard)
    elif callback_query.data == 'timetable_week':
        text = '<b>Расписание на текущую неделю</b>\n\nИспользование:\n<code>/week</code>'
        generate_callback_query_template(text, callback_query)
    elif callback_query.data == 'timetable_nextweek':
        text = '<b>Расписание на следующую неделю</b>\n\nИспользование:\n<code>/nextweek</code>'
        generate_callback_query_template(text, callback_query)
    elif callback_query.data == 'timetable_today':
        text = '<b>Расписание на сегодня</b>\n\nИспользование:\n<code>/today</code>'
        generate_callback_query_template(text, callback_query)
    elif callback_query.data == 'timetable_tomorrow':
        text = '<b>Расписание на завтра</b>\n\nИспользование:\n<code>/tomorrow</code>'
        generate_callback_query_template(text, callback_query)
