from pyrogram.types import Message


def get_command_arguments(message: Message, expected_arguments_count: int) -> str or list[str]:
    arguments = message.text.split(" ", expected_arguments_count)[1:]

    if len(arguments) == 1:
        return arguments[0]
    else:
        return arguments


def check_empty_arguments(message: Message, command: str, bot_username: str, error: str) -> bool:
    if message.text == f"/{command}" or message.text == f"/{command}@{bot_username}":
        message.reply_text(text=error)
        return True
    else:
        return False
