import time
from os import listdir


class Base_url:
    def __init__(self):
        self.base_url = "."
        self.files = listdir(self.base_url)
        self.file_name = "manage.py"

    def calc(self):
        while True:

            self.files = listdir(self.base_url)
            self.base_url += "/"
            if self.file_name in self.files:
                if self.base_url == ".":
                    self.base_url += "/"
                print(self.base_url)
                return self.base_url
            else:
                print(self.files)
                print(self.base_url)
                time.sleep(1)
            self.base_url += "../"



# from settings.test import Base_url
#
base = Base_url()
print(base.calc())