from config.app import app
from handlers import help_handler, keyboard_handler
from modules.reminder.lessons_parser import add_scheduled_tasks, scheduler
from modules.queue.handlers import queue_handler
from modules.reminder.handlers import db_handler
from modules.timetable.handlers import timetable_handler
from modules.tools.handlers import tools_handler


add_scheduled_tasks()
scheduler.start()
app.run()
