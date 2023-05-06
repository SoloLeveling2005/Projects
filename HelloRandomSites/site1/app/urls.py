from django.contrib import admin
from django.urls import path, include, re_path

from app import views

urlpatterns = [
    path("", views.index, name="index"),
    # # path("/get_book/<int:id_book>", views.get_book, name="get_book")
    # re_path(r'^api/get_book/(?P<book_id>\d+)/$', views.get_book, name="get_book"),
    # re_path(r'^api/get_book/$', views.get_book, name="get_book"),
]