from django.urls import path
from messenger import consumers

websocket_urlpatterns = [
    path('ws/<slug:room_name>/<str:user>/', consumers.ChatConsumer.as_asgi())
]
