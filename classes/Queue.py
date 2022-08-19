class User:
    def __init__(self, user_id, first_name, username=None, last_name=None):
        self.user_id = user_id
        self.first_name = first_name
        self.username = username
        self.last_name = last_name

    def __str__(self):
        return f"{self.first_name}{f' {self.last_name}' if self.last_name else ''} {f'(@{self.username})' if self.username else ''}"


class BotQueue:
    def __init__(self, name, creator_id):
        self.name = name
        self.members = []
        self.creator_id = creator_id
