from pyrogram import filters

from config.config import chat_id, admin_user_id, bot_username
from config.app import app
from config.errors import *
from classes.Queue import User, BotQueue
from functions.bot_functions import get_command_arguments, check_empty_arguments

current_queues = []


# создание новой очереди
@app.on_message(filters.group & filters.command(["create", f"create@{bot_username}"]) & filters.chat([chat_id]))
def create_queue(client, message):
    command = "create"

    is_empty_arguments = check_empty_arguments(message, command, bot_username, EMPTY_CREATE_QUEUE_ARGUMENT)

    # если пользватель вызвал команду с аргументом (не пустую)
    if not is_empty_arguments:
        name_args = get_command_arguments(message, 1)

        # есть ли очередь с таким названием
        is_dublicate = False
        # проверяем, есть ли очередь с таким названием
        if len(current_queues) != 0:
            # итерируемся через очереди
            for queue in current_queues:
                # если название совпало
                if queue.name == name_args:
                    # названия совпали
                    is_dublicate = True
                    # пишем пользователю
                    message.reply_text(text=f"Очередь с названием <b>{name_args}</b> уже существует.")
                    break

        # если названия не совпали
        if not is_dublicate:
            # создаём класс новой очереди (с именем и айди создателя очереди)
            new_queue = BotQueue(name=name_args, creator_id=message.from_user.id)
            # добавляем класс очереди в массив
            current_queues.append(new_queue)
            # оповещаем пользователя о создани очереди
            message.reply_text(text=f"Очередь с названием <code>{new_queue.name}</code> успешно создана.")


# добавить пользователя в очередь
@app.on_message(filters.group & filters.command(["join", f"join@{bot_username}"]) & filters.chat([chat_id]))
def join_queue(client, message):
    command = "join"

    is_empty_arguments = check_empty_arguments(message, command, bot_username, EMPTY_JOIN_QUEUE_ARGUMENT)

    # если пользватель вызвал команду с аргументом (не пустую)
    if not is_empty_arguments:
        name_args = get_command_arguments(message, 1)

        # если очередей нет (нет куда записыватся)
        if len(current_queues) == 0:
            message.reply_text(text="Сейчас нет активных очередей, в которые ты можешь записатся")
        # если есть очереди
        else:
            # найдена ли очередь с названием аргумента
            is_found = False

            # итерируемся через все очереди
            for queue in current_queues:
                # если название очереди совпало с названием аргумента
                if queue.name == name_args:
                    # создаем обьект пользователя
                    user = User(message.from_user.id, message.from_user.first_name, message.from_user.username if message.from_user.username else None, message.from_user.last_name if message.from_user.last_name else None)
                    # добавляем пользователя в эту очередь
                    queue.members.append(user)
                    # реплаем ему
                    message.reply_text(text=f"Ты успешно записался в очередь <b>{queue.name}</b>")
                    # очередь найдена
                    is_found = True
                    # выходим из цикла
                    break

            if not is_found:
                message.reply_text(text=f"Не удалось найти очередь <b>{name_args}</b>. Проверь, правильно ли ты ввел(-а) название.")


# посмотреть активные очереди
@app.on_message(filters.group & filters.command(["check", f"check@{bot_username}"]) & filters.chat([chat_id]))
def check_queues(client, message):
    # сообщение, которым будет отвечать бот (генерируется динамически)
    message_to_print = ""
    # если длинна маасива == 0 (пустой)
    if len(current_queues) == 0:
        message_to_print += "Сейчас нет активных очередей"
    else:
        message_to_print += f"Активных очередей: <b>{len(current_queues)}</b>\n\n"
        # итерируемся через массив current_queues
        for queue in current_queues:
            message_to_print += f"Название очереди: <b>{queue.name}</b>\n"
            # если участников очереди > 0 (массив с участниками не пустой)
            if len(queue.members) != 0:
                # итерируемся через массив с участниками
                for member in queue.members:
                    # добавляем к сообщению номер участника и его данные
                    message_to_print += f"{queue.members.index(member) + 1}) {member}\n"
            # добавляем перенос строки после блока с названием очереди
            message_to_print += "\n"

    message.reply_text(message_to_print)


# выход из очереди
@app.on_message(filters.group & filters.command(["leave", f"leave@{bot_username}"]) & filters.chat([chat_id]))
def leave_queue(client, message):
    command = "leave"

    is_empty_arguments = check_empty_arguments(message, command, bot_username, EMPTY_LEAVE_QUEUE_ARGUMENT)

    # если пользватель вызвал команду с аргументом (не пустую)
    if not is_empty_arguments:
        name_args = get_command_arguments(message, 1)

        if len(current_queues) == 0:
            message.reply_text(text="Сейчас нет активных очередей,из которых ты можешь выйти")
        else:
            is_found_queue = False
            is_found_user = False
            # итерируемся через лист с очередями
            for queue in current_queues:
                if queue.name == name_args:
                    is_found_queue = True
                    # итерируемся через лист с обьектами пользователей
                    for member in queue.members:
                        # если айди пользователя в листе и айди пользователя который отправил сообщения совпадает
                        if member.user_id == message.from_user.id:
                            is_found_user = True
                            # убираем его с листа
                            queue.members.pop(queue.members.index(member))
                            message.reply_text(text="Ты успешно вышел(-а) из очереди.")
                            # выходим из циклов
                            break

            # если очередь с таким именем не найдена, уведомляем об этом пользователя
            if not is_found_queue:
                message.reply_text(text=f"Не удалось найти очередь <b>{name_args}</b>. Проверь, правильно ли ты ввел(-а) название.")
            if not is_found_user:
                message.reply_text(text=f"Не удалось найти тебя в очереди <b>{name_args}</b>. Проверь, правильно ли ты ввел(-а) название.")


# удаление очереди
@app.on_message(filters.group & filters.command(["delete", f"delete@{bot_username}"]) & filters.chat([chat_id]))
def delete_queue(client, message):
    command = "delete"

    is_empty_arguments = check_empty_arguments(message, command, bot_username, EMPTY_DELETE_QUEUE_ARGUMENT)

    # если пользватель вызвал команду с аргументом (не пустую)
    if not is_empty_arguments:
        # получаем аргументы от коммадны (название очереди)
        name_args = get_command_arguments(message, 1)

        if len(current_queues) == 0:
            message.reply_text(text="Сейчас нет активных очередей, которые ты можешь удалить")
        else:
            is_found = False
            # итерируемся через лист с обьктами очередей
            for queue in current_queues:
                # если название очереди совпало с тем, что ввел пользователь
                if queue.name == name_args:
                    is_found = True
                    # если айди создателя в классе очереди совпадает с айди пользователя или айди создателя
                    if message.from_user.id == queue.creator_id or message.from_user.id == admin_user_id:
                        # удаляем этот обьект очереди
                        current_queues.pop(current_queues.index(queue))
                        # пишем пользователю
                        message.reply_text(text=f"Ты успешно удалил(-а) очередь <b>{name_args}</b>.")
                        break
                    # если айди не совпадают
                    else:
                        message.reply_text(text=f"У тебя нет права удалить эту очередь, так как ты не являешься её создателем.")
                        break
            # если очередь с таким именем не найдена, уведомляем об этом пользователя
            if not is_found:
                message.reply_text(text=f"Не удалось найти очередь <b>{name_args}</b>. Проверь, правильно ли ты ввел(-а) название.")


# пропустить человека в очереди
@app.on_message(filters.group & filters.command(["pass", f"pass@{bot_username}"]) & filters.chat([chat_id]))
def pass_queue(client, message):
    command = "pass"

    is_empty_arguments = check_empty_arguments(message, command, bot_username, EMPTY_PASS_QUEUE_ARGUMENT)

    # если пользватель вызвал команду с аргументом (не пустую)
    if not is_empty_arguments:
        args_array = get_command_arguments(message, 2)

        if args_array[0].lstrip("-").isdigit():
            index_to_pass = int(args_array[0])

            if index_to_pass > 0:
                message.reply_text("Количество людей для пропуска не может быть отрицательным числом.")
                return
        else:
            message.reply_text("Первый аргумент должен быть числом.\nПример: <code>/pass <кол-во мест> <название очереди></code>")
            return

        # получаем навзание очереди из аргументов
        queue_name = args_array[1]

        # если количество людей для пропуска очереди меньше 1 то выводим ошибку
        if index_to_pass < 1:
            message.reply_text("Количество людей для пропуска не может быть отрицательным числом.")
        else:
            # найдена ли очередь
            is_found_queue = False
            # изначальный индекс очереди в которой состоит человек
            i_queues_index = None
            # изначальный индекс человека в массиве с очередями
            i_users_index = None

            # итерируемся через лист с очередями
            for queue in current_queues:
                if queue.name == queue_name:
                    is_found_queue = True
                    # итерируемся через лист с обьектами пользователей
                    for member in queue.members:
                        # если айди пользователя в листе и айди пользователя который отправил сообщения совпадает
                        if member.user_id == message.from_user.id:
                            i_queues_index = current_queues.index(queue)
                            i_users_index = queue.members.index(member)
                            break

            if not is_found_queue:
                message.reply_text(f"Не удалось найти очередь <b>{queue_name}</b>. Проверь, правильно ли ты ввел(-а) название.")
            elif i_users_index is None:
                message.reply_text(f"Не удалось найти тебя в очереди <b>{queue_name}</b>. Проверь, правильно ли ты ввел(-а) название.")
            else:
                # перемещаем пользователя вниз
                current_queues[i_queues_index].members.insert(i_users_index + index_to_pass, current_queues[i_queues_index].members.pop(i_users_index))
                message.reply_text(f"Успешно переместил тебя на {index_to_pass} позиций вниз.")


# ресетнуть все очереди
@app.on_message(filters.group & filters.command(["reset", f"reset@{bot_username}"]) & filters.chat([chat_id]))
def reset(client, message):
    if message.from_user.id != admin_user_id:
        message.reply_text("У тебя нет права на использование этой команды.")
        return

    current_queues.clear()
    message.reply_text("Очистил все очереди.")
