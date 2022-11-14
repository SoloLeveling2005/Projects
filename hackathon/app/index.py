import datetime
import threading

import requests as requests
from flask import Flask, render_template, request, session1, url_for, redirect
import psycopg2
import time
import os
import re
from random import randint
import sqlite3 as sql
from bs4 import BeautifulSoup
import certifi

app = Flask(__name__, template_folder="templates")

# certifi.where()

# req = requests.get("https://jusan.kz/exchange-rates", verify=False, headers={
#     "User-Agent": 'My User Agent 1.0'})
#
# soup = BeautifulSoup(req.content, 'html.parser')
# new = soup.findAll('div',class_="inline currency-buy-table")
# print(new)
import requests

top = requests.Session()
top.verify = False
top.post(url='https://foo.com', data={'bar': 'baz'})
print(top)


@app.route("/", methods=['POST', 'GET'])
def home():
    return render_template('home.html')


# flask --app
if __name__ == '__main__':
    app.run(host='localhost', port=5000, debug=True)
