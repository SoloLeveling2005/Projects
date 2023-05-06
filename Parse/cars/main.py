import sys
import time

import requests
from bs4 import BeautifulSoup
import json
from threading import Thread
import asyncio

animation = ["[■□□□□□□□□□]", "[■■□□□□□□□□]", "[■■■□□□□□□□]", "[■■■■□□□□□□]", "[■■■■■□□□□□]", "[■■■■■■□□□□]",
             "[■■■■■■■□□□]", "[■■■■■■■■□□]", "[■■■■■■■■■□]", "[■■■■■■■■■■]"]

url = 'https://avto-russia.ru/autos/'
req = requests.get(url, timeout=10).text
# with open("htmls.txt", "w", encoding='utf-8') as file:
#     file.write(str(req))
# print(req)
global_data = []
global_id = 0
soup = BeautifulSoup(req, 'html.parser')
lists_marks = soup.find("div", class_="tab-content").find_all("div", {"class": "list-group col-sm-3 col-xs-6"})
print(len(lists_marks))


def get_car_url_1(url_car, url_two, title_mark):
    global global_id
    car_url = url_car['href']
    car_href = url_two + "/" + car_url
    req_three = requests.get(car_href, timeout=10).text
    soup_three = BeautifulSoup(req_three, 'html.parser')
    title_car = soup_three.find("div", class_="content").find("h1").text
    url_car_img = \
        soup_three.find("div", class_="item active").find("img", class_="img-responsive center-block")['src']
    info_car_trs = soup_three.find("table", class_="table table-striped table-condensed").find_all("tr")
    car_info = []
    for info_car_tr in info_car_trs:
        info_car_td = info_car_tr.find_all("td")
        car_info.append([info_car_td[0].text, info_car_td[1].text])
    info_car_description = soup_three.find("div", class_="text-left").find_all("p")[1].text.split("\n")[1]
    # print(title_mark)
    # print(title_car)
    # print(car_href)
    # print(car_info)
    global_data.append({
        'global_id': global_id,
        'title_mark': title_mark,
        'title_car': title_car,
        'car_href': car_href,
        'car_info': car_info,
        'car_description': info_car_description,
    })

    global_id += 1


def get_car_url_2(url_car, url_two, title_mark):
    global global_id
    two_url_car_arh = url_car['href']

    car_href_arh = url_two + "/" + two_url_car_arh
    req_three = requests.get(car_href_arh, timeout=10).text
    soup_three = BeautifulSoup(req_three, 'html.parser')
    title_car = soup_three.find("div", class_="content").find("h1").text
    url_car_img = \
        soup_three.find("div", class_="item active").find("img", class_="img-responsive center-block")['src']
    info_car_trs = soup_three.find("table", class_="table table-striped table-condensed").find_all("tr")
    car_info = []
    for info_car_tr in info_car_trs:
        info_car_td = info_car_tr.find_all("td")
        car_info.append([info_car_td[0].text, info_car_td[1].text])
    info_car_description = soup_three.find("div", class_="text-left").find_all("p")[1].text.split("\n")[1]
    # print(title_mark)
    # print(title_car)
    # print(car_href_arh)
    # print(car_info)
    global_data.append({
        'global_id': global_id,
        'title_mark': title_mark,
        'title_car': title_car,
        'car_href': car_href_arh,
        'car_info': car_info,
        'car_description': info_car_description,
    })
    global_id += 1


async def get_data(href_to_mark):
    global global_id
    title_mark = href_to_mark.text
    href_to_mark_url = href_to_mark['href']
    url_two = 'https://avto-russia.ru/autos/' + href_to_mark_url
    req_two = requests.get(url_two, timeout=10).text
    soup_two = BeautifulSoup(req_two, 'html.parser')
    urls_cars = soup_two.find_all("a", {"class": "thumbnail gallery-thumbnail"})
    print(url_two)

    for url_car in urls_cars:
        # print("treading1")
        try:
            Thread(target=get_car_url_1, args=(url_car, url_two, title_mark,)).run()
        except Exception as e:
            print(e)
    for url_car in urls_cars:
        # print("treading2")
        try:
            Thread(target=get_car_url_2, args=(url_car, url_two, title_mark,)).run()

        except Exception as e:
            print(e)


for list_marks in lists_marks:
    hrefs_to_mark = list_marks.find_all("a", {"class": "list-group-item"})
    print(hrefs_to_mark)
    for href_to_mark_get in hrefs_to_mark:
        asyncio.run(get_data(href_to_mark_get, ))
        with open(f'datas/data{global_id}.json', 'w') as f:
            json.dump(global_data, f)
        # t = Thread(target=get_data, args=(href_to_mark_get,))
        # t.run()

# while t.is_alive():  # пока функция выполняется
#     time.sleep(1)

#
# headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36'}
# proxy = {
#     "https": 'https://190.61.88.147:8080',
#     "http": 'http://190.61.88.147:8080'
# }
# url = 'https://auto.mail.ru/catalog/audi/'
#
# req = requests.get(url).text
# global_index = 0
# main_data = []
# # print(req)
# with open("htmls.txt", "w", encoding='utf-8') as file:
#     file.write(str(req))
# soup = BeautifulSoup(req, 'html.parser')
# print(soup)
# marks = soup.find_all("a", {"class": "p-firm__text link-holder"})
# for mark in marks:
#     print(mark.title)
#     url_catalog = 'https://auto.mail.ru' + mark['href']
#     # print(url_catalog)
#     req_catalog = requests.get(url_catalog)
#     soup_catalog = BeautifulSoup(req_catalog.text, 'html.parser')
#     cars_info = soup_catalog.find_all("div", {"class": "p-car p-car_catalog-firm margin_bottom_20"})
#     for car in cars_info:
#         car_info_img_url = soup_catalog.find_all("img", {"class": "p-car__image"})
#         car_info_title = soup_catalog.find_all("a", {"class": "p-car__title link-holder"})
#         # print(car_info_img_url)
#         # print(car_info_title)
#         # print(len(car_info_img_url))
#         # print(len(car_info_title))
#         index = 0
#         while len(car_info_img_url) - 1 >= index:
#             src = car_info_img_url[index]['src']
#             title = car_info_title[index].text
#             # print(src)
#             # print(title)
#
#             main_data.append({
#                 "id": global_index,
#                 "mark": f'{mark.text}',
#                 "title": f"{title}",
#                 "description": "Очень крутая машинка",
#                 "estimation": "4.9",
#                 "stars": "★★★★★",
#                 "img_url": f"{src}",
#                 "more_info": ["инфо", "инфо", "инфо", "инфо"]
#             })
#             index += 1
#             global_index += 1
#
#         # for i in car_info_img_url:
#         #     print(i['src'])
#         # for i in car_info_title:
#         #     print(i.text)
#
# print(main_data)
print(global_data)
with open('data_main.json', 'w') as f:
    json.dump(global_data, f)
