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


def find_chat_threading(message, bot):
    applications_thread = threading.Thread(target=find_chat, args=(message, bot,))
    applications_thread.daemon = True
    applications_thread.start()


def find_chat(message, bot):
    user_id = message.chat.id
    while True:

        with sql.connect('todo.db') as con:
            cur = con.cursor()
            cur.execute(f"""
                            SELECT * FROM connection_couple WHERE first = {user_id};
                        """)
            user = cur.fetchall()
        if user:
            bot.send_message(message.chat.id,
                             f"Нашел, ваш собеседник онлайн",
                             parse_mode='HTML')

        time.sleep(1)
