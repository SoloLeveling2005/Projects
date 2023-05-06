import sqlite3


class Main:
    def __init__(self, BASE_DIR):
        self.BASE_DIR = BASE_DIR
        self.connect = None

    def local_create_connect(self):
        self.connect = sqlite3.connect(f"{self.BASE_DIR}/database/UserData.db")

    def local_create_table(self):
        cur = self.connect.cursor()
        cur.execute("CREATE TABLE IF NOT EXISTS user(title, year, score)")
        self.connect.commit()


