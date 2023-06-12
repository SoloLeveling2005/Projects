# import requests
#
# API_URL = "https://api-inference.huggingface.co/models/CompVis/stable-diffusion-v1-4"
# headers = {"Authorization": "Bearer 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"}
#
#
# def query(payload):
#     response = requests.post(API_URL, headers=headers, json=payload)
#     return response.content
#
#
# image_bytes = query({
#     "inputs": "Cool programmer",
# })
# # You can access the image with PIL.Image for example
# import io
# from PIL import Image
#
# image = Image.open(io.BytesIO(image_bytes))
# image.show()


import requests

API_URL = "https://api-inference.huggingface.co/models/stabilityai/stable-diffusion-2"
headers = {"Authorization": "Bearer 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"}


def query(payload):
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.content


image_bytes = query({
    "inputs": "A high tech solarpunk utopia in the Amazon rainforest",
})
# You can access the image with PIL.Image for example
import io
from PIL import Image

image = Image.open(io.BytesIO(image_bytes))
image.show()
