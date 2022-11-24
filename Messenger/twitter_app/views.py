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

from django.views.decorators.csrf import csrf_exempt

from twitter_app.models import Tweets, Rating, Users


def get_user_data(user_id: int = None, user_nickname: str = None, user_password: str = None,
                  according_data: str = None):
    """
    according_data - по каким данным искать

    в случае ошибки вернет None
    """
    try:
        if according_data == "user_id":
            return Users.objects.get(id=user_id)
        elif according_data == "user_nickname/user_password":
            return Users.objects.get(user_nickname=user_nickname, user_password=user_password)
        else:
            return None
    except Exception as e:
        print(e)
        return None


def get_likes_user(user_id: int):
    """
    Функция возвращает массив id твитов, которые лайкнул пользователь с id = user_id
    в случае ошибки вернет None
    """
    try:
        mass_likes_user = []
        for like_user in Rating.objects.filter(user_id=user_id):
            mass_likes_user.append(like_user.id_tweet)
        return mass_likes_user
    except Exception as e:
        print(e)
        return None


@csrf_exempt
def log_auth(request: HttpRequest, context=None) -> HttpResponse:
    if request.method == "GET":
        context = {}
        user_id = request.COOKIES.get('user_id')
        if user_id is None:
            return render(request, 'public/twitter_app/log_auth.html', context)
        else:
            return redirect(reverse('twitter_app:home', args=(user_id,)))
    elif request.method == "POST":
        if 'input_nickname_auth' in request.POST:
            nickname = request.POST.get('input_nickname_auth', "")
            password = request.POST.get('input_password_auth', "")
            print(nickname)
            print(password)
            user_id = get_user_data(user_nickname=nickname, user_password=password,
                                    according_data="user_nickname/user_password")
            if user_id is None:
                context = {'data': json.dumps({"error": "Такого пользователя не существует"})}
                print("Такого пользователя не существует")
                return render(request, 'public/twitter_app/log_auth.html', context=context)
            else:
                home_page = redirect(reverse('twitter_app:home', args=()))
                home_page.set_cookie('user_id', user_id.id, max_age=60 * 20)
                return home_page

        elif 'input_nickname' in request.POST:
            name = request.POST.get('input_name', "")
            nickname = request.POST.get('input_nickname', "")
            password = request.POST.get('input_password', "")
            repeat_password = request.POST.get('input_repeat_password', "")

            if password != repeat_password:
                context = {'data': json.dumps({"error": "Пароли не совпадают"})}
                print("Пароли не совпадают")
                return render(request, 'public/twitter_app/log_auth.html', context=context)

            if name and nickname and password:
                if get_user_data(user_nickname=nickname, user_password=password,
                                 according_data="user_nickname/user_password"):
                    context = {json.dumps({"error": "Пользователь с такими данными уже существует"})}
                    print("Пользователь с такими данными уже существует")
                    return render(request, 'public/twitter_app/log_auth.html')

                Users.objects.create(
                    user_name=name,
                    user_nickname=nickname,
                    user_password=password,
                )

                user_id = get_user_data(user_nickname=nickname, user_password=password,
                                        according_data="user_nickname/user_password").id
                home_page = redirect(reverse('twitter_app:home', args=()))
                home_page.set_cookie('user_id', user_id, max_age=60 * 20)
                return home_page
            else:
                context = {'data': json.dumps({"error": "поля не заполнены!"})}
                print("поля не заполнены!")
                return render(request, 'public/twitter_app/log_auth.html', context=context)


def home(request: HttpRequest) -> HttpResponse:
    if request.method == "GET":
        user_id = request.COOKIES.get('user_id')
        print("Я дома")
        if user_id is None:
            return redirect(reverse('twitter_app:log_auth', args=()))
        else:
            user_data = get_user_data(user_id=user_id, according_data="user_id")  # получаем данные пользователя по id
            likes_user = get_likes_user(user_id=user_id)  # твиты которые лайкнул юзер
            tweets = list(Tweets.objects.filter(parent_tweet_id=None).values())  # твиты которые не имеют родителя
            print(tweets)

            return render(request, 'public/twitter_app/home.html',
                          context={'user_id': user_id, 'user_data': user_data, 'tweets': tweets,
                                   'likes_user': likes_user})

# @csrf_exempt
# def new_tweet(request: HttpRequest) -> Union[HttpResponseBadRequest, JsonResponse]:
#     if request.method == 'POST':
#         author_id = request.POST.get('author_id', None)
#         tweet_text = request.POST.get('tweet_text', None)
#         parent_tweet_id = request.POST.get('parent_tweet_id', None)
#         print(parent_tweet_id)
#         author = Users.objects.get(id=int(author_id))
#         if parent_tweet_id == None:
#             Tweets.objects.create(author_id=author_id, author_nickname=author.user_nickname,
#                                   text_tweet=tweet_text, likes=0)
#         else:
#             post = Tweets.objects.get(id=parent_tweet_id)
#             post.comments += 1
#             post.save()
#             Tweets.objects.create(author_id=author_id, author_nickname=author.user_nickname,
#                                   text_tweet=tweet_text, likes=0, parent_tweet_id=parent_tweet_id)
#             return redirect(reverse('twitter_app:check_tweet', args=(author_id, parent_tweet_id,)))
#         return redirect(reverse('twitter_app:home', args=(author_id,)))
#         # return JsonResponse({'status': 'Todo added!'})
#     return JsonResponse({'status': 'Invalid request'}, status=400)
#
#
# def get_info_new_tweet(request: HttpRequest, code: int):
#     if request.method == 'GET':
#         print(Tweets.objects.all())
#         todos = list(Tweets.objects.all().values())
#         print(todos)
#         return JsonResponse({'context': todos})
#     return JsonResponse({'status': 'Invalid request'}, status=400)
#
#
# def get_info_tweet(request: HttpRequest):
#     if request.method == 'GET':
#         print(Tweets.objects.all())
#         todos = list(Tweets.objects.all().values())
#         print(todos)
#         return JsonResponse({'context': todos})
#     return JsonResponse({'status': 'Invalid request'}, status=400)
#
#
# def like_tweet(request: HttpRequest, user_id: int, id_tweet: int, parent_id_tweet: int, parent_user_id: int):
#     if request.method == 'GET':
#         print("user_id", user_id)
#         print("id_tweet", id_tweet)
#         # print(Rating.objects.get(user_id=user_id))
#         post = Tweets.objects.get(id=id_tweet)
#         author_id = post.author_id
#         try:
#             print(Rating.objects.get(user_id=user_id, id_tweet=id_tweet))
#             post.likes = Tweets.objects.get(id=id_tweet).likes - 1
#             post.save()
#             Rating.objects.get(user_id=user_id, id_tweet=id_tweet).delete()
#             if parent_id_tweet == 0:
#                 return redirect(reverse('twitter_app:home', args=(author_id,)))
#             else:
#                 print("Вернулся")
#                 return redirect(reverse('twitter_app:check_tweet', args=(parent_user_id, parent_id_tweet,)))
#         except:
#             Rating.objects.create(
#                 id_tweet=id_tweet,
#                 user_id=user_id,
#             )
#
#             post.likes = Tweets.objects.get(id=id_tweet).likes + 1
#             post.save()
#             if parent_id_tweet == 0:
#                 return redirect(reverse('twitter_app:home', args=(author_id,)))
#             else:
#                 return redirect(reverse('twitter_app:check_tweet', args=(parent_user_id, parent_id_tweet,)))
#     return JsonResponse({'status': 'Invalid request'}, status=400)
#     # return render(request, 'django_twitter_app/home.html', context=context)
#
#
# def delete_tweet(request: HttpRequest, id_user: int, id_tweet: int):
#     context = {}
#     if request.method == 'GET':
#         print(id_tweet)
#         post = Tweets.objects.get(id=id_tweet)
#         author_id = post.author_id
#         if id_user == author_id:
#             Rating.objects.filter(id_tweet=id_tweet).delete()
#             post.delete()
#             return redirect(reverse('twitter_app:home', args=(author_id,)))
#         else:
#             return redirect(reverse('twitter_app:home', args=(id_user,)))
#     return JsonResponse({'status': 'Invalid request'}, status=400)
#
#
# #
# #
# #
# #
# #
#
#
# def home(request: HttpRequest, code: int = 0) -> HttpResponse:
#     if request.method == "GET":
#         user_id = request.COOKIES.get('user_id')
#         print("Я дома")
#         if user_id is None:
#             return redirect(reverse('log_auth:log_auth', args=()))
#         else:
#             if int(user_id) == int(code):
#                 likes_user = Rating.objects.filter(user_id=user_id)
#                 mass_likes_user = []
#                 for like_user in likes_user:
#                     mass_likes_user.append(like_user.id_tweet)
#                 print(mass_likes_user)
#                 # todos = list(Tweets.objects.all().values())
#                 todos = list(Tweets.objects.filter(parent_tweet_id=None).values())
#
#                 mass_comments_user = []
#                 for like_user in likes_user:
#                     mass_comments_user.append(like_user.id_tweet)
#                 print(mass_comments_user)
#
#                 print(todos)
#                 user_nickname = Users.objects.get(id=user_id).user_nickname
#                 return render(request, 'public/twitter_app/home.html',
#                               context={'user_id': user_id, 'content': todos, 'user_nickname': user_nickname,
#                                        'mass_likes_user': mass_likes_user, 'mass_comments_user': mass_comments_user,
#                                        })
#             else:
#                 return redirect(reverse('twitter_app:home', args=(user_id,)))
#
#
# def check_tweet(request: HttpRequest, user_id: int, id_tweet: int):
#     if request.method == "GET":
#         cookie_user_id = request.COOKIES.get('user_id')
#         if cookie_user_id is None:
#             return redirect(reverse('log_auth:log_auth', args=()))
#         else:
#
#             likes_user = Rating.objects.filter(user_id=cookie_user_id)
#             mass_likes_user = []
#             for like_user in likes_user:
#                 mass_likes_user.append(like_user.id_tweet)
#
#             tweets = Tweets.objects.filter(parent_tweet_id=id_tweet)
#             user_data = Users.objects.get(id=cookie_user_id)
#             try:
#                 this_tweet = Tweets.objects.get(id=id_tweet)
#             except:
#                 this_tweet = []
#             return render(request, 'public/twitter_app/check_tweet.html',
#                           context={'content': tweets, 'user_data': user_data,
#                                    'mass_likes_user': mass_likes_user, 'this_tweet': this_tweet,
#                                    'this_id_tweet': id_tweet, 'this_user_id': cookie_user_id})
#
#
# def check_user(request: HttpRequest, user_id: int):
#     if request.method == "GET":
#         cookie_user_id = request.COOKIES.get('user_id')
#         if cookie_user_id is None:
#             return redirect(reverse('log_auth:log_auth', args=()))
#         else:
#             tweets = Tweets.objects.filter(author_id=user_id)
#             user_data = Users.objects.get(id=cookie_user_id)
#             if int(user_id) == int(cookie_user_id):
#                 return render(request, 'public/twitter_app/check_user.html',
#                               context={'tweets': tweets, 'user_data': user_data, 'admin': 'true', 'user_id':user_id})
#             else:
#                 return render(request, 'public/twitter_app/check_user.html',
#                               context={'tweets': tweets, 'user_data': user_data, 'admin': 'false', 'user_id':user_id})
