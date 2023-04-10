import sqlite3
from typing import List
import sys
import time
from nltk.tokenize import sent_tokenize, word_tokenize
from colorama import Fore, Style
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize



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

        self.stemmer = PorterStemmer()

        # create db
        self.bot = sqlite3.connect(f"{path}{name}.db")
        self.bot_cursor = self.bot.cursor()

        # create tables
        self.bot_cursor.executescript("""
                CREATE TABLE IF NOT EXISTS answers(
                    id INTEGER PRIMARY KEY,
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

    def train(self, data):
        """
        :param data: [{'question':'', 'answer':''},{'question':'', 'answer':''}}]
        :return: Тренировка модели.
        """
        # Режем массив вопросов
        for one_data in data:
            answer = self.bot_cursor.execute(f"""
                            INSERT INTO answers (answer) VALUES
                                ("{one_data['answer']}")
                        """)
            answer_id = answer.lastrowid
            self.write_in_db_tokens(data=one_data, primary_key=answer_id)
        self.bot.commit()

    def speak(self, question: str = ""):
        pass

    def write_in_db_tokens(self, data, primary_key):

        data = data['question']
        print(primary_key)
        result = [
            self.bot_cursor.execute(f"""
                    INSERT INTO question_tokens(token,answer_id) VALUES
                        ("{i}", {primary_key})
                """)
            for i in [self.stemmer.stem(word) for word in word_tokenize(data)]
        ]

    @staticmethod
    def training_animation():
        for i in range(10, 101, 10):
            time.sleep(0.3)
            progress_bar = "Обучение модели: [{}{}] {}%".format("=" * int(i / 10), " " * (10 - int(i / 10)), i)
            sys.stdout.write('\r' + progress_bar)
            sys.stdout.flush()
        print("")

    def __del__(self):
        # закрываем соединение с базой данных
        self.bot.close()
