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

from log_auth.models import Users



# Create your views here.
def log_auth(request: HttpRequest, context=None) -> HttpResponse:
    if request.method == "GET":
        context = {}
        user_id = request.COOKIES.get('user_id')
        if user_id is None:
            return render(request, 'public/twitter_app/log_auth.html', context)
        else:
            return redirect(reverse('twitter_app:home', args=(user_id,)))
    elif request.method == "POST":
        print(request.POST)
        if 'input_nickname_auth' in request.POST:
            # TODO получить с формы данные
            nickname = request.POST.get('input_nickname_auth', "")
            password = request.POST.get('input_password_auth', "")
            print(nickname)
            print(password)
            try:
                print("До сюда дошел")
                post_name = Users.objects.get(user_nickname=nickname, user_password=password)
                print(post_name.user_nickname)
                print(post_name.user_password)
            except:
                context = {"error": "Такого пользователя не существует"}
                context = {'data': json.dumps(context)}
                return render(request, 'public/twitter_app/log_auth.html', context=context)

            home_page = redirect(reverse('twitter_app:home', args=(post_name.id,)))
            home_page2 = redirect(reverse('todo_app:home', args=(post_name.id,)))

            home_page.set_cookie('user_id', post_name.id, max_age=60 * 5)
            home_page2.set_cookie('user_id', post_name.id, max_age=60 * 5)
            return home_page

        elif 'input_nickname' in request.POST:
            # TODO получить с формы данные
            nickname = request.POST.get('input_nickname', "")
            password = request.POST.get('input_password', "")
            repeat_password = request.POST.get('input_repeat_password', "")

            if password != repeat_password:
                context = {"error": "Пароли не совпадают"}
                context = {'data': json.dumps(context)}
                return render(request, 'public/twitter_app/log_auth.html', context=context)

            if nickname or password:
                try:
                    post_name = Users.objects.get(user_nickname=nickname, user_password=password)
                    context = {"error": "Пользователь с таким никнеймом уже существует"}
                    context = {'data': json.dumps(context)}
                    print("Пользователь с таким никнеймом уже существует")
                    return render(request, 'public/twitter_app/log_auth.html', context=context)
                except:
                    pass

                # current_dt = (str(datetime.datetime.now()).replace(' ', '').replace(':', '').replace('-', '').replace(
                #     '.', ''))[11:] + str(randint(10, 99))
                Users.objects.create(
                    user_nickname=nickname,
                    user_password=password,
                )
                new_user_id = Users.objects.get(user_nickname=nickname, user_password=password).id
                home_page = redirect(reverse('twitter_app:home', args=(new_user_id,)))
                home_page2 = redirect(reverse('todo_app:home', args=(new_user_id,)))
                home_page.set_cookie('user_id', new_user_id, max_age=60 * 5)
                home_page2.set_cookie('user_id', new_user_id, max_age=60 * 5)
                return home_page
            else:
                context = {"error": "поля не заполнены!"}
                context = {'data': json.dumps(context)}
                print("поля не заполнены!")
                return render(request, 'public/twitter_app/log_auth.html', context=context)
