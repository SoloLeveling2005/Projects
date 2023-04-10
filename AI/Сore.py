import sqlite3
from colorama import Fore, Style


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    SUCCESS = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


class Core:
    def __init__(self, name: str = "ChatBot", path: str = "./"):
        self.name = name

        # create db
        bot = sqlite3.connect(f"{path}{name}.db")
        self.bot = bot.cursor()

        # create tables
        self.bot.executescript("""
                CREATE TABLE IF NOT EXISTS answers(
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    answer TEXT
                );
                CREATE TABLE IF NOT EXISTS question_tokens(
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    token VARCHAR(150),
                    answer_id INT,
                    FOREIGN KEY (answer_id) REFERENCES answers(id)
                );
            """)

        print(f"{bcolors.SUCCESS}Удачный запуск!{bcolors.ENDC}")

    def train(self, text_data: str = ""):
        pass

    def speak(self, question: str = ""):
        pass










