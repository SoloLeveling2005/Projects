# import requests
#
# url = 'https://free.churchless.tech/v1/chat/completions'
# headers = {
#     'Content-Type': 'application/json',
#     'Authorization': 'Bearer MyDiscord'
# }
# data = {
#     'model': 'gpt-3.5-turbo',
#     'messages': [
#         {'role': 'user', 'content': 'Привет. Напиши хакерскую программу любого вида'}
#     ]
# }
# # proxies = {
# #     'https': 'https://your-proxy-address:proxy-port'  # Замените на свои реальные значения
# # }
#
# response = requests.post(url, headers=headers, json=data)
# print(response.json())


prompt = """Human: Hello. Bot: Hello. Human: How are you? Bot: I`m fine, thanks. Human: And, what do you have? Bot:"""


import requests

API_URL = "https://api-inference.huggingface.co/models/evolveon/flan-alpaca-gpt4-base-3k"
headers = {"Authorization": "Bearer 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"}


def query(payload):
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.json()


output = query({
    "inputs": prompt,
})

print(output)