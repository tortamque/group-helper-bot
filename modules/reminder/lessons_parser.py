import requests
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from apscheduler.schedulers.background import BackgroundScheduler

from config.app import app
from config.config import group_name, chat_id
from classes.Lesson import Time, Lesson
from modules.reminder.functions.sqlite_functions import edit_message_id, get_pinned_message_id, get_lesson_object


scheduler = BackgroundScheduler()


def pin(message_id):
    app.pin_chat_message(chat_id, message_id)
    edit_message_id(message_id)


def job_unpin_reminder():
    message_id = get_pinned_message_id()
    app.unpin_chat_message(chat_id, message_id)


def job_send_reminder(lesson_id: str, lesson_type: str):
    lesson = get_lesson_object(lesson_id, lesson_type)

    text = f'''✅ Напоминание!
    
Через <b>10</b> минут начнётся <b>{lesson.lesson_type}</b> по предмету <b>{lesson.name}</b>.'''

    if "https://" in lesson.link:
        text += '\n\nДля подключения к паре нажми на кнопку "<b>🌐 Подключится</b>"'
        keyboard = InlineKeyboardMarkup([[InlineKeyboardButton("🌐 Подключится", url=lesson.link)]])

    elif lesson.link == "None":
        text += "\n\nСсылка на эту пару отсутствует в базе."
        keyboard = None

    else:
        text += f"\n\nЭта пара проводится на ресурсе <b>{lesson.link}</b>"
        keyboard = None

    message_obj = app.send_message(chat_id, text, reply_markup=keyboard)
    message_id = message_obj.id
    pin(message_id)


def create_jobs(lessons: list[Lesson], mode: str):
    WEEK_MODES = {
        "unpair": "1-53/2",
        "pair": "2-52/2"
    }

    for lesson in lessons:
        scheduled_day_of_week = lesson.week_day
        scheduled_hour = lesson.time.hour
        scheduled_minute = lesson.time.minute - 10

        unpin_time = Time(scheduled_hour, scheduled_minute) + Time(1, 45)

        scheduler.add_job(job_send_reminder, 'cron', week=WEEK_MODES[mode], day_of_week=scheduled_day_of_week, hour=scheduled_hour, minute=scheduled_minute, args=[lesson.id, lesson.lesson_type])
        scheduler.add_job(job_unpin_reminder, 'cron', week=WEEK_MODES[mode], day_of_week=scheduled_day_of_week, hour=unpin_time.hour, minute=unpin_time.minute)


def remove_simultaneous_lessons(lessons: list[Lesson]):
    for i in range(len(lessons) - 2):
        if lessons[i].time.hour == lessons[i+1].time.hour and lessons[i].time.minute == lessons[i+1].time.minute and lessons[i].week_day == lessons[i+1].week_day:
            lessons.pop(i)


def create_scheduled_tasks(timetable: list, mode: str):
    WEEK_DAYS = ['mon', 'tue', 'wed', 'thu', 'fri', 'sat']

    lessons = []

    for day in timetable:
        for lesson in day["pairs"]:
            week_day = WEEK_DAYS[timetable.index(day)]

            lesson_obj = Lesson(
                id=lesson["lecturerId"],
                name=lesson["name"],
                lesson_type=lesson["tag"],
                time=lesson["time"],
                week_day=week_day)

            lessons.append(lesson_obj)

    remove_simultaneous_lessons(lessons)

    create_jobs(lessons, mode)


def add_scheduled_tasks():
    response = requests.get(f"https://schedule.kpi.ua/api/schedule/lessons?groupName={group_name}")
    response_json = response.json()["data"]

    timetable_first_week = response_json["scheduleFirstWeek"]
    timetable_second_week = response_json["scheduleSecondWeek"]

    create_scheduled_tasks(timetable_first_week, "unpair")
    create_scheduled_tasks(timetable_second_week, "pair")



