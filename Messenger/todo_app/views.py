import json
from typing import Union

from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User, Group
from django.http import HttpRequest, HttpResponse, JsonResponse, HttpResponseBadRequest
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View
from random import randint
import datetime

from todo_app import models
from todo_app.models import Tasks
from log_auth.models import Users



def complete_task(request: HttpRequest, task_id:int):
    if request.method == "GET":
        author_id = Tasks.objects.get(id=task_id).author_id
        task = Tasks.objects.get(id=task_id)
        task.done = True
        task.save()
        return redirect(reverse('todo_app:home', args=(author_id,)))
    
def delete_task(request: HttpRequest, task_id: int):
    pass

def new_task(request: HttpRequest, user_id:int):
    if request.method == "POST":
        title = request.POST.get('title', "")
        description = request.POST.get('description', "")

        if title == "" or description == "":
            print("Данные пустые")
            print(title)
            print(description)
            return redirect(reverse('todo_app:home', args=(user_id,)))
        Tasks.objects.create(
            author_id=user_id,
            task_title=title,
            task_description=description,
            done=False
        )
        return redirect(reverse('todo_app:home', args=(user_id,)))

def home(request: HttpRequest, user_id: int = 0) -> HttpResponse:
    if request.method == "GET":
        cookies_user_id = request.COOKIES.get('user_id')
        print(cookies_user_id)
        if cookies_user_id is None:
            return redirect(reverse('log_auth:log_auth', args=()))
        else:
            if int(cookies_user_id) == int(user_id):
                todos = list(Tasks.objects.all().values())
                print(todos)
                return render(request, 'public/todo_app/home.html', context={'user_id': cookies_user_id, 'content': todos})
            else:
                return redirect(reverse('todo_app:home', args=(cookies_user_id,)))
