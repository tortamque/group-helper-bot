import sqlite3

from classes.Lesson import Lesson


def connect_db():
    connection = sqlite3.connect('modules/reminder/database/db.db')
    cursor = connection.cursor()

    return connection, cursor


def get_lessons_ids():
    connection, cursor = connect_db()

    query_id = 'SELECT id FROM lessons_links'
    record_id = cursor.execute(query_id).fetchall()

    ids = [lesson_id[0] for lesson_id in record_id]

    names = []
    for lesson_id in ids:
        query_name = 'SELECT name FROM lessons_links WHERE id = ?'
        record_name = cursor.execute(query_name, (lesson_id,)).fetchall()

        names.append(record_name[0][0])

    types = []
    for lesson_type in ids:
        query_name = 'SELECT type FROM lessons_links WHERE id = ?'
        record_name = cursor.execute(query_name, (lesson_type,)).fetchall()

        types.append(record_name[0][0])

    cursor.close()

    return ids, names, types


def edit_link(query_id, new_link):
    connection, cursor = connect_db()

    cursor.execute('UPDATE lessons_links SET link = ? WHERE id = ?', (new_link, query_id))
    connection.commit()
    cursor.close()


def get_pinned_message_id():
    connection, cursor = connect_db()

    query = 'SELECT id FROM pinned_message_id'
    record = cursor.execute(query).fetchone()[0]
    cursor.close()

    return record


def edit_message_id(new_message_id):
    connection, cursor = connect_db()
    cursor.execute('UPDATE pinned_message_id SET id = ?', (new_message_id,))
    connection.commit()
    cursor.close()


def get_lesson_object(lesson_id: str, lesson_type: str) -> Lesson:
    connection, cursor = connect_db()
    db_lesson_id = f"{lesson_id}_{lesson_type}"

    query_name = 'SELECT name FROM lessons_links WHERE id = ?'
    record_name = cursor.execute(query_name, (db_lesson_id,)).fetchone()
    lesson_name = record_name[0]

    query_type = 'SELECT type FROM lessons_links WHERE id = ?'
    record_type = cursor.execute(query_type, (db_lesson_id,)).fetchone()
    lesson_type = record_type[0]

    query_link = 'SELECT link FROM lessons_links WHERE id = ?'
    record_link = cursor.execute(query_link, (db_lesson_id,)).fetchone()
    lesson_link = record_link[0]

    lesson = Lesson(
        id=lesson_id,
        name=lesson_name,
        lesson_type=lesson_type,
        link=lesson_link)

    return lesson
