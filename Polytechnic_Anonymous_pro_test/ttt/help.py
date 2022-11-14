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

from connect import bot

from aiogram import Bot, Dispatcher, executor, types
from aiogram.types.message import ContentType

# log
logging.basicConfig(level=logging.INFO)

# init
dp = Dispatcher(bot)

# prices
PRICE = types.LabeledPrice(label="Подписка на 1 месяц", amount=500 * 100)  # в копейках (руб)


# buy
@dp.message_handler(commands=['buy'])
async def buy(message: types.Message):
    if config.PAYMENTS_TOKEN.split(':')[1] == 'TEST':
        await bot.send_message(message.chat.id, "Тестовый платеж!!!")

    await bot.send_invoice(message.chat.id,
                           title="Подписка на бота",
                           description="Активация подписки на бота на 1 месяц",
                           provider_token=config.PAYMENTS_TOKEN,
                           currency="rub",
                           photo_url="https://www.aroged.com/wp-content/uploads/2022/06/Telegram-has-a-premium-subscription.jpg",
                           photo_width=416,
                           photo_height=234,
                           photo_size=416,
                           is_flexible=False,
                           prices=[PRICE],
                           start_parameter="one-month-subscription",
                           payload="test-invoice-payload")


# pre checkout  (must be answered in 10 seconds)
@dp.pre_checkout_query_handler(lambda query: True)
async def pre_checkout_query(pre_checkout_q: types.PreCheckoutQuery):
    await bot.answer_pre_checkout_query(pre_checkout_q.id, ok=True)


# successful payment
@dp.message_handler(content_types=ContentType.SUCCESSFUL_PAYMENT)
async def successful_payment(message: types.Message):
    print("SUCCESSFUL PAYMENT:")
    payment_info = message.successful_payment.to_python()
    for k, v in payment_info.items():
        print(f"{k} = {v}")

    await bot.send_message(message.chat.id,
                           f"Платёж на сумму {message.successful_payment.total_amount // 100} {message.successful_payment.currency} прошел успешно!!!")


# run long-polling
if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=False)



# @bot.message_handler(content_types=["voice", "video", "document", "sticker", "photo", "text"])
# def get_message(message):
#     print("Есть контакт")
#     if message.content_type == 'voice':
#         audio_id = message.voice.file_id
#         bot.send_audio(message.chat.id, audio_id)
#         print(audio_id)
#     elif message.content_type == 'video':
#         video_id = message.video.file_id
#         bot.send_video(message.chat.id, video_id)
#         print(video_id)
#     elif message.content_type == "document":
#         document_id = message.document.file_id
#         bot.send_document(message.chat.id, document_id)
#         print(document_id)
#     elif message.content_type == "sticker":
#         sticker_id = message.sticker.file_id
#         bot.send_sticker(message.chat.id, sticker_id)
#         print(sticker_id)
#     elif message.content_type == "photo":
#         img = message.photo[0].file_id
#         bot.send_photo(message.chat.id, img)
#         print(img)
#     elif message.content_type == "text":
#         print(message)
#         bot.send_message(message.chat.id,
#                          message.text)
#
