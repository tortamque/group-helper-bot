class Time:
    def __init__(self, hour: int, minute: int):
        self.hour = hour
        self.minute = minute

    def __str__(self):
        return f"{self.hour}:{self.minute}"

    def __add__(self, other):
        hour = self.hour + other.hour
        minute = self.minute + other.minute

        if minute >= 60:
            hour += 1
            minute -= 60

        return Time(hour, minute)


class Lesson:
    def __init__(self, id: str, name: str, lesson_type: str, time: None or str = None, week_day: None or str = None, link: None or str = None, teacher: None or str = None):
        self.id = id
        self.name = name

        if lesson_type == "lec":
            self.lesson_type = "Лекція"
        elif lesson_type == "prac":
            self.lesson_type = "Практика"
        elif lesson_type == "lab":
            self.lesson_type = "Лабораторна"
        elif lesson_type == "Лекція" or lesson_type == "Практика" or lesson_type == "Лабораторна":
            self.lesson_type = lesson_type
        else:
            self.lesson_type = None

        if time is not None:
            self.time = Time(hour=int(time.split('.')[0]), minute=int(time.split('.')[1]))

        self.week_day = week_day
        self.link = link
        self.teacher = teacher

    def __eq__(self, other):
        return self.name == other.name and self.lesson_type == other.lesson_type and self.time == other.time and self.week_day == other.week_day and self.link == other.link

    def __hash__(self):
        return hash(self.id and self.name and self.lesson_type)
