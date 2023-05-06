import requests

token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJhY2Nlc3NJRCI6ImM2YjVhOWZjLWNkZDgtNGVlMS05N2E0LTA1OTg0YWU5OTI0YSJ9.yVjdq8vM3W3qO0WmVLsVh-KPYR1d_UT6uzApYydWCxo"
# token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJhY2Nlc3NJRCI6IjMxYWFkYWU5LTcwMTgtNDg2Ny05NzA0LTIxODIyM2YwMTQwYSJ9.guYP6MgIvjHrFKdugJQRnd0-Y7kLk0YEwYtBnES59_E"


warehouse = "https://suppliers-api.wildberries.ru/api/v2/warehouses"
url_ids = "https://suppliers-api.wildberries.ru/public/api/v1/info"
url = 'https://statistics-api.wildberries.ru/api/v1/supplier/incomes?dateFrom=2023-01-28'
headers = {
    'accept': 'application/json',
    'Authorization': token
}
# Родины

response = requests.get(url, headers=headers)

if response.status_code == 200:
    data = response.json()
    print(data)
    print("len: ", len(data))
    for i in data:
        print(i)
    # print(response.json())
else:
    print(response.headers)
    print(f"Request failed with status code: {response.status_code}")

