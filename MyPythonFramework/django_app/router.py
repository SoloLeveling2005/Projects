import os
import sys
from basic.router import Router


class App(Router):
    def __init__(self):
        super().__init__()
        self.path_dir = ""
        Router.create_rout(self, name="index", path="/")
        Router.create_rout(self, name="main", path="/main")
        Router.create_rout(self, name="home", path="/home")

    def index(self):
        return self.pattern('index.html')

    def main(self):
        return self.pattern('main.html')

    def home(self):
        return self.pattern('home.html')

# controller.create_rout(name="index", path="/", url_file="index.html")


# @controller.method(path="/", name="")
# def index():
#
#     return controller.give_me_file_url("index.html")
#
# def index1():
#
#     return "1"

# wrapped_func = index.__wrapped__
# print(wrapped_func)

# print(controller.mass_urls)


# Create an empty list to store decorated functions


# Iterate over all the functions in the current module

# print(controller.dr)
# a = 9
# print(controller.__class__)
# print(controller)
