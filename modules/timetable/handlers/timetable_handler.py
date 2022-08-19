from pyrogram import filters
import datetime
import calendar
import requests

from config.config import chat_id, group_name, bot_username
from config.app import app
from modules.timetable.functions.timetable_functions import generate_weekly_timetable, generate_daily_timetable


# расписание звонков
@app.on_message(filters.group & filters.command(["timetable", f"timetable@{bot_username}"]) & filters.chat([chat_id]))
def timetable(client, message):
    message.reply_text("<i>1 пара</i>  08-30 - 10-05\n<i>2 пара</i>  10-25 - 12-00\n<i>3 пара</i>  12-20 - 13-55\n<i>4 пара</i>  14-15 - 15-50\n<i>5 пара</i>  16-10 - 17-45")


# присылание полного расписания на неделю
@app.on_message(filters.group & filters.command(["week", f"week@{bot_username}"]) & filters.chat([chat_id]))
def week(client, message):
    # получаем номер сегодняшней недели
    week_number = datetime.date.today().isocalendar()[1]

    response = requests.get(f"https://schedule.kpi.ua/api/schedule/lessons?groupName={group_name}")
    response_json = response.json()["data"]

    # если неделя парная
    if week_number % 2 == 0:
        timetable_first_week = response_json["scheduleFirstWeek"]

        text = generate_weekly_timetable(timetable_first_week)
    # если неделя непарная
    else:
        timetable_second_week = response_json["scheduleSecondWeek"]

        text = generate_weekly_timetable(timetable_second_week)

    message.reply_text(text=text)


# присылание расписания на следующую неделю
@app.on_message(filters.group & filters.command(["nextweek", f"nextweek@{bot_username}"]) & filters.chat([chat_id]))
def nextweek(client, message):
    # получаем номер следующей недели
    week_number = datetime.date.today().isocalendar()[1] + 1

    response = requests.get(f"https://schedule.kpi.ua/api/schedule/lessons?groupName={group_name}")
    response_json = response.json()["data"]

    # если неделя парная
    if week_number % 2 == 0:
        timetable_first_week = response_json["scheduleFirstWeek"]

        text = generate_weekly_timetable(timetable_first_week)
    # если неделя непарная
    else:
        timetable_second_week = response_json["scheduleSecondWeek"]

        text = generate_weekly_timetable(timetable_second_week)

    message.reply_text(text=text)


# присылание расписания на сегодня
@app.on_message(filters.group & filters.command(["today", f"today@{bot_username}"]) & filters.chat([chat_id]))
def today(client, message):
    # получаем номер следующей недели
    week_number = datetime.date.today().isocalendar()[1] + 1
    today_name = calendar.day_abbr[datetime.date.today().weekday()]

    response = requests.get(f"https://schedule.kpi.ua/api/schedule/lessons?groupName={group_name}")
    response_json = response.json()["data"]

    # если неделя непарная (первая неделя, но после войны парная)
    if week_number % 2 == 0:
        timetable_first_week = response_json["scheduleFirstWeek"]

        text = generate_daily_timetable(timetable_first_week, today_name)
    else:
        timetable_second_week = response_json["scheduleSecondWeek"]

        text = generate_daily_timetable(timetable_second_week, today_name)

    message.reply_text(text=text)


# присылание расписания на завтра
@app.on_message(filters.group & filters.command(["tomorrow", f"tomorrow@{bot_username}"]) & filters.chat([chat_id]))
def tomorrow(client, message):
    # получаем номер следующей недели
    week_number = datetime.date.today().isocalendar()[1] + 1
    tomorrow_name = calendar.day_abbr[(datetime.date.today() + datetime.timedelta(days=1)).weekday()]

    response = requests.get(f"https://schedule.kpi.ua/api/schedule/lessons?groupName={group_name}")
    response_json = response.json()["data"]

    # если неделя непарная (первая неделя, но после войны парная)
    if week_number % 2 == 0:
        timetable_first_week = response_json["scheduleFirstWeek"]

        text = generate_daily_timetable(timetable_first_week, tomorrow_name)
    else:
        timetable_second_week = response_json["scheduleSecondWeek"]

        text = generate_daily_timetable(timetable_second_week, tomorrow_name)

    message.reply_text(text=text)
