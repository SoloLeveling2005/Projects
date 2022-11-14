import requests
from random import randint
import sqlite3 as sql
from bs4 import BeautifulSoup
import certifi


req = requests.get("https://jusan.kz/exchange-rates", verify=False, headers={
    "User-Agent": 'My User Agent 1.0'})

soup = BeautifulSoup(req.content, 'lxml')

# print(soup.decode())




r = requests.get('https://jusan.kz/exchange-rates', auth=('user', 'pass'), verify=False,)
print(r.text)