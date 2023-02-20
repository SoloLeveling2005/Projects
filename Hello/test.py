import random
import sys
import threading
import codecs
import time
import tkinter as tk

import pyautogui

# Получаем ширину и высоту экрана
screen_width, screen_height = pyautogui.size()




import webview

"""
This example demonstrates how to retrieve a DOM element
"""


# def get_elements(window):
#     content = window.get_elements('.pywebview-drag-region')
#     # print('Heading:\n %s ' % heading[0]['outerHTML'])
#     # print('Content 1:\n %s ' % content[0]['outerHTML'])
#     print(content)
#
# if __name__ == '__main__':
#
#     window = webview.create_window("Hello world", "http://127.0.0.1:8000", frameless=True, width=screen_width, height=screen_height)
#     webview.start(get_elements, window)
#



class Api:
    def __init__(self):
        self.cancel_heavy_stuff_flag = False

    def init(self):
        response = {
            'message': 'Hello from Python {0}'.format(sys.version)
        }
        return response

    def getRandomNumber(self):
        response = {
            'message': 'Here is a random number courtesy of randint: {0}'.format(random.randint(0, 100000000))
        }
        return response

    def doHeavyStuff(self):
        time.sleep(0.1)  # sleep to prevent from the ui thread from freezing for a moment
        now = time.time()
        self.cancel_heavy_stuff_flag = False
        for i in range(0, 1000000):
            _ = i * random.randint(0, 1000)
            if self.cancel_heavy_stuff_flag:
                response = {'message': 'Operation cancelled'}
                break
        else:
            then = time.time()
            response = {
                'message': 'Operation took {0:.1f} seconds on the thread {1}'.format((then - now), threading.current_thread())
            }
        return response

    def cancelHeavyStuff(self):
        time.sleep(0.1)
        self.cancel_heavy_stuff_flag = True

    def sayHelloTo(self, name):
        response = {
            'message': 'Hello {0}!'.format(name)
        }
        return response

    def error(self):
        raise Exception('This is a Python exception')



if __name__ == '__main__':
    api = Api()
    window = webview.create_window('API example', "http://127.0.0.1:8000", js_api=api)
    webview.start()
import webview
import webview.menu as wm

"""
This example demonstrates how to create an application menu
"""


def change_active_window_content():
    active_window = webview.active_window()
    if active_window:
        active_window.load_html('<h1>You changed this window!</h1>')

def click_me():
    active_window = webview.active_window()
    if active_window:
        active_window.load_html('<h1>You clicked me!</h1>')

def do_nothing():
    pass

def say_this_is_window_2():
    active_window = webview.active_window()
    if active_window:
        active_window.load_html('<h1>This is window 2</h2>')

def open_file_dialog():
    active_window = webview.active_window()
    active_window.create_file_dialog(webview.SAVE_DIALOG, directory='/', save_filename='test.file')


if __name__ == '__main__':
    window_1 = webview.create_window('Application Menu Example', 'https://pywebview.flowrl.com/hello')
    window_2 = webview.create_window('Another Window', html='<h1>Another window to test application menu</h1>')

    menu_items = [
        wm.Menu(
            'Test Menu',
            [
                wm.MenuAction('Change Active Window Content', change_active_window_content),
                wm.MenuSeparator(),
                wm.Menu(
                    'Random',
                    [
                        wm.MenuAction('Click Me', click_me),
                        wm.MenuAction('File Dialog', open_file_dialog)
                    ]
                )
            ]
        ),
        wm.Menu(
            'Nothing Here',
            [
                wm.MenuAction('This will do nothing', do_nothing)
            ]
        )
    ]

    webview.start(menu=menu_items)