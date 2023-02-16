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

    def check(self, data_listen: str):
        # self.tokens = nltk.word_tokenize(data_listen)
        self.tokens = data_listen.split(" ")
        for command in self.built_in_command:
            print(self.tokens)
            if command.lower() in self.tokens:
                new_window_message(self.built_in_command[command])
                print(command.lower())
                return True
        else:
            return False

    def coincidence(self):
        pass

