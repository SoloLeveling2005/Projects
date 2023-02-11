from controller import Controller


class Core:
    # todo расходы/доходы
    # todo задачи (id, title, description, data_add, deadline)
    # todo календарь
    # todo цели

    # msg = await self.client.wait_for('message', check=lambda m: m.channel == self.message_client.channel and
    # m.author.id == self.message_client.author.id) /// msg.content

    def __init__(self):
        self.errors = {
            "undefined": "Команда не распознана, скорректируйте запрос.",
            "none": "Команда не точная, скорректируйте запрос"
        }

        self.commands = {
            "help": ["help"],
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
        self.controller = Controller(self.commands)
        self.commands_help = {
            "**Узнать доступные команды**": "help",
            "**Добавить цель**": "new_goal",
            "**Распечатать ваши цели**": "get_goals",
        }

    def core_controller(self, obj, message):
        """
        :param obj: Подается объект с которым будет производиться какое-либо действие
        :param message: Пришедшее сообщение от пользователя
        :return:
        """
        method_name = self.controller.calculate(message=message)
        method = getattr(obj, method_name)
        return method()


# class Users(Core):
#     def __init__(self):
#         self.users = []



class User(Core):
    def __init__(self, client):
        super().__init__()
        self.client = client
        # self.message_client = message
        self.goals = []

    def error(self):
        pass

    def help(self):
        print("\033[33m{}\033[37m".format("help command"))

        message = ""
        for command in self.commands_help:
            message += f"{command}:\n"
            for i in self.commands[self.commands_help[command]]:
                message += f"- {i} \n"
        return message

    def new_goal(self, message):
        user.new_goal()

        # self.message_client.channel.send("Цель добавлена.")
        self.goals.append(text)
        return "Цель добавлена."

    def get_goals(self):
        return self.goals
