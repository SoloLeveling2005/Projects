import time
import os
import re
from random import randint
import telebot
from telebot import types  # кнопки Telegram
import datetime
import threading
import sqlite3 as sql
import json



def what_do_you_do(message,what):
    user_id = message.chat.id
    with sql.connect('todo.db') as con:
        cur = con.cursor()
        cur.execute(f"""
                        UPDATE do SET where_you = "{what}" WHERE user_id = {user_id}
                    """)




def update_connection_chat_threading():
    applications_thread = threading.Thread(target=update_connection_chat)
    applications_thread.daemon = True
    applications_thread.start()


def update_connection_chat():
    while True:
        with sql.connect('todo.db') as con:
            cur = con.cursor()
            cur.execute(f"""SELECT * FROM request_connections_couple""")
            users = cur.fetchall()
        if users:
            if len(users) > 2:
                first = users[0][0]
                second = users[0][1]

