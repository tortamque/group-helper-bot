from classes.Lesson import Lesson


def generate_weekly_timetable(timetable):
    text = ""

    for day in timetable:
        lessons = []

        text += f"<b>{day['day']}</b>\n"

        for lesson in day['pairs']:
            lessons.append(
                Lesson(
                    id="1",
                    name=lesson['name'],
                    lesson_type=lesson['tag'],
                    time=lesson['time'],
                    teacher=lesson['teacherName']
                )
            )

        lessons.sort(key=lambda lesson_arr: lesson_arr.time.hour)

        for lesson in lessons:
            text += f"{lesson.time.hour}:{lesson.time.minute}) {lesson.name}\n{lesson.teacher}\n{lesson.lesson_type}\n\n"

        text += '\n'

    return text


def generate_daily_timetable(timetable, todays_day):
    DAYS = {
        'Mon': 'Пн',
        'Tue': 'Вв',
        'Wed': 'Ср',
        'Thu': 'Чт',
        'Fri': 'Пт',
        'Sat': 'Сб',
        'Sun': 'Нд'
    }

    text = ''

    for day in timetable:
        text += f"<b>{DAYS[todays_day]}</b>\n"

        if todays_day == 'Sun':
            text += "Сегодня отдыхаем"

            break
        elif day['day'] == DAYS[todays_day]:

            lessons = []

            for lesson in day['pairs']:
                lessons.append(
                    Lesson(
                        id="1",
                        name=lesson['name'],
                        lesson_type=lesson['tag'],
                        time=lesson['time'],
                        teacher=lesson['teacherName']
                    )
                )

            lessons.sort(key=lambda lesson_arr: lesson_arr.time.hour)

            for lesson in lessons:
                text += f"{lesson.time.hour}:{lesson.time.minute}) {lesson.name}\n{lesson.teacher}\n{lesson.lesson_type}\n\n"

            break

    return text
