import sqlite3


class Core:
    def __init__(self, name: str = "ChatBot", path: str = "./"):
        self.name = name
        self.bot = sqlite3.connect(f"{path}{name}.db")
        self.token = sqlite3.connect(f"{path}token.db")

    def train(self, text_data: str = ""):
        pass

    def speak(self, question: str = ""):
        pass






