import nltk
from message import new_window_message


class Core:
    def __init__(self):
        self.tokens = None
        self.built_in_command = {
            "Помощь": "Команды для помощи",
            "Создать": {
                "Команду": ""
            }
        }

    def coincidence(self, data_listen: str):
        # self.tokens = nltk.word_tokenize(data_listen)
        self.tokens = data_listen.strip().split(" ")
        for token in self.tokens:
            for command in self.built_in_command:
                # todo, учитываем длину, количество слов. Если символов 7 то макс погрешность 3

                nltk.edit_distance(command.lower())
                # if command.lower() in self.tokens:
                #     new_window_message(self.built_in_command[command])
                #     print(command.lower())
                #     return True

