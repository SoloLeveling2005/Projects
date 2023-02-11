class Core:
    # todo расходы/доходы
    # todo задачи (id, title, description, data_add, deadline)
    # todo календарь
    # todo цели

    def __init__(self):
        self.commands = {
            "new_goal": [
                "Добавьте цель",
                "Добавь цель",
                "Добавить цель",
                "Задайте цель",
                "Установите цель",
                "Объявите цель",
                "Укажите цель"
            ],
            "get_goals": [
                "какие цели у меня были",
                "напомни о моих целях",
                "дай цели",
                "выведи цели"
            ],
        }

    def controller(self, obj, method_name, **kwargs):
        method = getattr(obj, method_name)

        method()


class Users(Core):
    def __init__(self):
        self.users = []
        super().__init__()


class User(Users):
    def __init__(self, client, message):
        super().__init__()
        self.client = client
        self.message_client = message
        self.goals = []

    def new_goal(self):
        msg = await self.client.wait_for('message',
            check=lambda m: m.channel == self.message_client.channel and m.author.id == self.message_client.author.id)
        user.new_goal(msg.content)

        await message.channel.send("Цель добавлена.")
        self.goals.append(text)

    def get_goals(self):
        return self.goals
