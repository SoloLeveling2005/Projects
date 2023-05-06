import asyncio
import json
from channels.generic.websocket import AsyncJsonWebsocketConsumer
from asgiref.sync import sync_to_async
from datetime import datetime, date, time

from django.core import serializers
from django.core.serializers.json import DjangoJSONEncoder

from messenger import models


def save_group(username, room, message):
    user = models.User.objects.get(name=username)
    room = models.Room.objects.get(slug=room)


class ChatConsumer(AsyncJsonWebsocketConsumer):

    async def get_messages(self, room_name):
        query_set = models.Message.objects.filter(room=room_name)
        serialized_data = await sync_to_async(serializers.serialize)("json", query_set)
        return serialized_data

    async def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = f'chat_{self.room_name}'
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )
        await self.accept()

        mess = await self.get_messages(self.room_name)
        await self.send(text_data=json.dumps({
            "room_message": mess
        }))

    async def disconnect(self, code):
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name,
        )

    async def receive(self, text_data):
        data = json.loads(text_data)
        method_ = data["method"]

        if method_ == 'post':
            message = data["message"]
            username = data["username"]
            room = data["room"]

            id = await self.save_message(username, room, message)
            await self.channel_layer.group_send(
                self.room_group_name,
                {
                    "type": "chat_message",
                    "id": id,
                    "message": message,
                    "username": username,
                    "room": room
                }
            )
        elif method_ == 'delete':
            id_ = data["id"]
            print('delete')
            await self.delete_message(id_)

            # await self.channel_layer.group_send(
            #     self.room_group_name,
            #     {
            #         "type": "chat_message",
            #         "id": id_,
            #         "message": "message",
            #         "username": "username",
            #         "room": "room"
            #     }
            # )
            await self.channel_layer.group_send(
                self.room_group_name,
                {
                    "type": "chat_message",
                    "id": id_,
                    "message": 'message',
                    "username": 'username',
                    "room": 'room'
                }
            )

    async def chat_message(self, event):
        message = event["message"]
        username = event["username"]
        room = event["room"]
        id = event["id"]

        await self.send(text_data=json.dumps({
            "message": message,
            "username": username,
            "room": room,
            "id": id
        }))

    @sync_to_async
    def save_message(self, username, room, message):
        user = models.User.objects.get(name=username)
        username = username
        room = models.Room.objects.get(slug=room)
        data_model = models.Message.objects.create(username=username, user=user, room=room, content=str(message))
        return data_model.id

    @sync_to_async
    def delete_message(self, id_):
        message_ = models.Message.objects.get(id=id_)
        message_.delete()
    # @sync_to_async
