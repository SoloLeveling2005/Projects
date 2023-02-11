import threading

import editdistance


class Controller:
    def __init__(self, commands):
        self.commands = commands
        self.response_options = []

    def calculate(self, message):
        """
        :return: Возвращается название действия
        """
        action = None
        threads = []
        for command in self.commands:
            t = threading.Thread(target=self.calc, kwargs={
                'command': command,
                'message': message
            })
            threads.append(t)
            t.start()

        for thread in threads:
            thread.join()
            # print("завершение потока2")

        print(self.response_options)
        if len(self.response_options) == 1:
            # todo Выполнить
            return self.response_options[0]
        elif len(self.response_options) == 0:
            # todo Такой команды нет
            return "undefined"
        else:
            # todo Команда не точная
            return "none"


    def calc(self, command, message):
        # print("self.commands:", self.commands)
        for text in self.commands[command]:
            length_mass = len(message.split(" "))
            distance = editdistance.distance(text, message)
            # print("distance:", distance, "/", text,":",message)
            # print("\n\n")
            if distance <= 2 or distance <= length_mass:
                print("command:", text)
                self.response_options.append(text)
        # print("завершение потока")

