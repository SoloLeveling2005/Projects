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


def get_example_tasks(request: HttpRequest):
    data = [[x * y * z for x in range(1, 6)] for y in range(1, 6) for z in range(1, 6)]
    return JsonResponse({'data': data})


def get_one_task(task_id):
    return Tasks.objects.get(id=task_id)


def get_all_tasks():
    return Tasks.objects.all()


def task_list(request: HttpRequest, task_id: int):
    pass


def task_detail(request: HttpRequest, task_id: int):
    task = get_one_task(task_id)
    if request.method == "GET":
        return render(request, 'public/todo_app/one.html', context={'content': task})


def complete_task(request: HttpRequest, task_id: int):
    if request.method == "GET":
        author_id = get_one_task(task_id).author_id
        task = get_one_task(task_id)
        task.done = True
        task.save()
        with open("logs.txt", "a") as myfile:
            myfile.write(f"- Пользователь {author_id} выполнил задачу {task_id}\n")
        return redirect(reverse('todo_app:home', args=(author_id,)))


def delete_task(request: HttpRequest, task_id: int):
    if request.method == "GET":
        author_id = Tasks.objects.get(id=task_id).author_id
        Tasks.objects.get(id=task_id).delete()
        with open("logs.txt", "a") as myfile:
            myfile.write(f"- Пользователь {author_id} удали задачу {task_id}\n")
        return redirect(reverse('todo_app:home', args=(author_id,)))


def new_task(request: HttpRequest, user_id: int):
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
        with open("logs.txt", "a") as myfile:
            myfile.write(f"- Пользователь {user_id} создал задачу\n")
        return redirect(reverse('todo_app:home', args=(user_id,)))


def home(request: HttpRequest, user_id: int = 0) -> HttpResponse:
    if request.method == "GET":
        cookies_user_id = request.COOKIES.get('user_id')
        print(cookies_user_id)
        if cookies_user_id is None:
            return redirect(reverse('log_auth:log_auth', args=()))
        else:
            if int(cookies_user_id) == int(user_id):
                todos = list(get_all_tasks().values())
                print(todos)

                return render(request, 'public/todo_app/home.html',
                              context={'user_id': cookies_user_id, 'content': todos})
            else:
                with open("logs.txt", "a") as myfile:
                    myfile.write("Начало работы\n")
                return redirect(reverse('todo_app:home', args=(cookies_user_id,)))
