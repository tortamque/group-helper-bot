import requests
from pyrogram import filters

from config.app import app
from config.config import group_name, chat_id, admin_user_id, bot_username
from modules.reminder.functions.sqlite_functions import connect_db, edit_link, get_lessons_ids
from functions.bot_functions import get_command_arguments
from classes.Lesson import Lesson


@app.on_message(filters.group & filters.command(["setup_db", f"setup_db@{bot_username}"]) & filters.chat([chat_id]))
def setup_db(client, message):
    if message.from_user.id != admin_user_id:
        message.reply_text("У тебя нет права на использование этой команды.")
        return

    lessons_set = set()

    response = requests.get(f"https://schedule.kpi.ua/api/schedule/lessons?groupName={group_name}")
    response_json = response.json()["data"]

    weeks = [response_json["scheduleFirstWeek"], response_json["scheduleSecondWeek"]]

    for week in weeks:
        for day in week:
            for pair in day["pairs"]:
                lesson = Lesson(
                    id=pair["lecturerId"],
                    name=pair["name"],
                    lesson_type=pair["tag"])

                lessons_set.add(lesson)

    connection, cursor = connect_db()

    for lesson in lessons_set:
        lesson_db_id = f"{lesson.id}_{lesson.lesson_type}"

        cursor.execute('INSERT INTO lessons_links (id, name, type, link) VALUES (?, ?, ?, ?)', (lesson_db_id, lesson.name, lesson.lesson_type, "None",))
        connection.commit()

    cursor.close()

    message.reply_text(text=f"База данных была успешно настроена.")


@app.on_message(filters.group & filters.command(["show_db", f"show_db@{bot_username}"]) & filters.chat([chat_id]))
def show_db(client, message):
    if message.from_user.id != admin_user_id:
        message.reply_text("У тебя нет права на использование этой команды.")
        return

    connection, cursor = connect_db()

    columns = [column[1] for column in cursor.execute('PRAGMA table_info(lessons_links)').fetchall()]
    whole_db = cursor.execute('SELECT * FROM lessons_links ').fetchall()

    cursor.close()

    output = ""

    for row in whole_db:
        output += f"""
<b>{columns[0]}</b>: <code>{row[0]}</code>
<b>{columns[1]}</b>: <code>{row[1]}</code>
<b>{columns[2]}</b>: <code>{row[2]}</code>
<b>{columns[3]}</b>: <code>{row[3]}</code>
"""

    message.reply_text(text=output)


@app.on_message(filters.group & filters.command(["reset_db", f"reset_db@{bot_username}"]) & filters.chat([chat_id]))
def reset_db(client, message):
    if message.from_user.id != admin_user_id:
        message.reply_text("У тебя нет права на использование этой команды.")
        return

    connection, cursor = connect_db()
    cursor.execute('DELETE FROM lessons_links')
    connection.commit()
    cursor.close()

    message.reply_text(text="База данных была успешно очищена.")


@app.on_message(filters.group & filters.command(["editlink", f"editlink@{bot_username}"]) & filters.chat([chat_id]))
def editlink(client, message):
    if message.from_user.id != admin_user_id:
        message.reply_text("У тебя нет права на использование этой команды.")
        return

    arguments = get_command_arguments(message, 2)

    lesson_id = arguments[0]
    new_link = arguments[1]

    edit_link(lesson_id, new_link)

    message.reply_text("Ссылка на пару была успешно изменена.")


@app.on_message(filters.group & filters.command(["ids", f"ids@{bot_username}"]) & filters.chat([chat_id]))
def send_ids(client, message):
    if message.from_user.id != admin_user_id:
        message.reply_text("У тебя нет права на использование этой команды.")
        return

    ids, names, types = get_lessons_ids()

    output = "Список доступных ID:\n\n"

    for lesson_id, lesson_name, lesson_type in zip(ids, names, types):
        output += f"<b>ID</b>: <code>{lesson_id}</code>\n{lesson_name}. {lesson_type}\n\n"

    message.reply_text(output)
