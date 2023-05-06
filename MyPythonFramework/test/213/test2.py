import requests

url = 'https://suppliers-api.wildberries.ru/api/v3/supplies?limit=12&next=1'
headers = {
    'accept': 'application/json',
    'Authorization': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJhY2Nlc3NJRCI6ImM2YjVhOWZjLWNkZDgtNGVlMS05N2E0LTA1OTg0YWU5OTI0YSJ9.yVjdq8vM3W3qO0WmVLsVh-KPYR1d_UT6uzApYydWCxo'
}

response = requests.get(url, headers=headers)
# curl -X GET "https://suppliers-api.wildberries.ru/api/v2/warehouses" -H "accept: application/json" -H "Authorization: eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJhY2Nlc3NJRCI6ImM2YjVhOWZjLWNkZDgtNGVlMS05N2E0LTA1OTg0YWU5OTI0YSJ9.yVjdq8vM3W3qO0WmVLsVh-KPYR1d_UT6uzApYydWCxo"
print(response)