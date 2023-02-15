# from twilio.twiml.messaging_response import MessagingResponse
# from flask import Flask, request
#
# app = Flask(__name__)
#
#
# @app.route("/whatsapp", methods=['POST'])
# def reply_whatsapp():
#     # Получение входящего сообщения и отправка ответа
#     msg = request.form.get('Body')
#     resp = MessagingResponse()
#     resp.message("Вы написали: {}".format(msg))
#     return str(resp)
#
#
#
#
# if __name__ == "__main__":
#     app.run(debug=True)


# from twilio.rest import Client
#
# account_sid = 'ACf6193f99e3f9ceb4f1f9f3553eaf4451'
# auth_token = '[AuthToken]'
# client = Client(account_sid, auth_token)
#
# message = client.messages.create(
#     from_='whatsapp:+14155238886',
#     body='Your appointment is coming up on July 21 at 3PM',
#     to='whatsapp:+77774208321'
# )
#
# print(message.sid)
#



# from twilio.rest import Client
#
# account_sid = 'ACf6193f99e3f9ceb4f1f9f3553eaf4451'
# auth_token = '[AuthToken]'
# client = Client(account_sid, auth_token)
#
# message = client.messages.create(
#     from_='whatsapp:+14155238886',
#     body='Your Twilio code is 1238432',
#     to='whatsapp:+77774208321'
# )
#
# print(message.sid)


from twilio.rest import Client

account_sid = 'ACf6193f99e3f9ceb4f1f9f3553eaf4451'
auth_token = 'bfa5e8b7f7863e4e2aaa5765175cb3c8'
client = Client(account_sid, auth_token)

message = client.messages.create(
    from_='whatsapp:+14155238886',
    body='Hello! This is an editable text message. You are free to change it and write whatever you like.',
    to='whatsapp:+77774208321'
)

print(message.sid)