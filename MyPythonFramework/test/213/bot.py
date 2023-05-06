import requests
from bs4 import BeautifulSoup

# адрес страницы авторизации
login_url = 'https://analitika-wb-ozon.pro/auth/'

# данные для авторизации
data = {
    'username': 'sellerDV2k6',
    'password': 'FC3beN0u27'
}

# создаем сессию
session = requests.Session()

# отправляем запрос на авторизацию
response = session.post(login_url, data=data)

# если авторизация прошла успешно, делаем запрос к защищенной странице
if response.status_code == 200:
    print()
    proxies = {
        'http': 'http://51.222.146.133:59166',
        'https': 'http://69.36.182.103:3897',
    }
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36'
    }

    url = 'https://analitika-wb-ozon.pro/'
    response = requests.get(url, proxies=proxies, headers=headers)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        # Ищем все теги <p> на странице и выводим их текст
        for p in soup.find_all('p'):
            print(p.text)
    else:
        print("Error: Unable to retrieve page")

else:
    print("Error: Unable to login")
