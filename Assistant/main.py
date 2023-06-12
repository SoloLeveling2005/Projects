import requests

url = 'https://free.churchless.tech/v1/chat/completions'
headers = {
    'Content-Type': 'application/json'
}
data = {
    'model': 'gpt-3.5-turbo',
    'messages': [
        {'role': 'user', 'content': 'Hello, how are you?'}
    ]
}
# proxies = {
#     'https': 'https://your-proxy-address:proxy-port'  # Замените на свои реальные значения
# }

response = requests.post(url, headers=headers, json=data)
print(response.json())
