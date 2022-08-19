from config.app import app

from handlers.help.main_page_help_handler import answer_main
from modules.queue.help.help_handler import answer_queue
from modules.reminder.help.help_handler import answer_db
from modules.timetable.help.help_handler import answer_timetable
from modules.tools.help.help_handler import answer_tools


@app.on_callback_query()
def answer(client, callback_query):
    main_callbacks = ['main']
    queue_callbacks = ['queue', 'create', 'delete', 'join', 'leave', 'check', 'pass', 'reset']
    db_callbacks = ['db', 'setup_db', 'show_db', 'reset_db', 'editlink', 'ids']
    timetable_callbacks = ['timetable', 'timetable_week', 'timetable_nextweek', 'timetable_today', 'timetable_tomorrow']
    tools_callbacks = ['tools', 'ping', 'chat_id', 'user_id']

    if callback_query.data in main_callbacks:
        answer_main(callback_query)

    elif callback_query.data in queue_callbacks:
        answer_queue(client, callback_query)

    elif callback_query.data in db_callbacks:
        answer_db(client, callback_query)

    elif callback_query.data in timetable_callbacks:
        answer_timetable(client, callback_query)

    elif callback_query.data in tools_callbacks:
        answer_tools(client, callback_query)
