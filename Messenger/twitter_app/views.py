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


from twitter_app.models import Tweets
from log_auth.models import Users


def new_tweet(request: HttpRequest) -> Union[HttpResponseBadRequest, JsonResponse]:
    if request.method == 'POST':
        id_tweet = (str(datetime.datetime.now()).replace(' ', '').replace(':', '').replace('-', '').replace(
            '.', ''))[11:] + str(randint(10, 99))
        author_id = request.POST.get('author_id', None)
        tweet_text = request.POST.get('tweet_text', None)
        author = Users.objects.get(user_id=int(author_id))
        Tweets.objects.create(id_tweet=id_tweet, author_id=author_id, author_nickname=author.user_nickname,
                              text_tweet=tweet_text, likes=0)
        return redirect(reverse('twitter_app:home', args=(author_id,)))
        # return JsonResponse({'status': 'Todo added!'})
    return JsonResponse({'status': 'Invalid request'}, status=400)


def get_info_new_tweet(request: HttpRequest, code: int):
    if request.method == 'GET':
        print(Tweets.objects.all())
        todos = list(Tweets.objects.all().values())
        print(todos)
        return JsonResponse({'context': todos})
    return JsonResponse({'status': 'Invalid request'}, status=400)


def get_info_tweet(request: HttpRequest):
    if request.method == 'GET':
        print(Tweets.objects.all())
        todos = list(Tweets.objects.all().values())
        print(todos)
        return JsonResponse({'context': todos})
    return JsonResponse({'status': 'Invalid request'}, status=400)


def like_tweet(request: HttpRequest, id_tweet: int):
    if request.method == 'GET':
        post = Tweets.objects.get(id_tweet=id_tweet)
        post.likes = Tweets.objects.get(id_tweet=id_tweet).likes + 1
        author_id = post.author_id
        post.save()
        return redirect(reverse('twitter_app:home', args=(author_id,)))
    return JsonResponse({'status': 'Invalid request'}, status=400)
    # return render(request, 'django_twitter_app/home.html', context=context)


def dislike_tweet(request: HttpRequest, id_tweet: int):
    if request.method == 'GET':
        author_id = Tweets.objects.get(id=id_tweet).author_id
        post = Tweets.objects.get(id=id_tweet)
        post.likes = Tweets.objects.get(id=id_tweet).likes - 1
        post.save()
        return redirect(reverse('twitter_app:home', args=(author_id,)))
    return JsonResponse({'status': 'Invalid request'}, status=400)
    # return render(request, 'django_twitter_app/home.html', context=context)


def delete_tweet(request: HttpRequest, id_tweet: int):
    context = {}
    if request.method == 'GET':
        post = Tweets.objects.get(id_tweet=id_tweet)
        author_id = post.author_id
        post.delete()
        return redirect(reverse('twitter_app:home', args=(author_id,)))
    return JsonResponse({'status': 'Invalid request'}, status=400)


#
#
#
#
#



def home(request: HttpRequest, code: int = 0) -> HttpResponse:
    if request.method == "GET":
        user_id = request.COOKIES.get('user_id')
        print("Я дома")
        if user_id is None:
            return redirect(reverse('log_auth:log_auth', args=()))
        else:
            if int(user_id) == int(code):
                todos = list(Tweets.objects.all().values())
                print(todos)
                return render(request, 'public/twitter_app/home.html', context={'user_id': user_id, 'content': todos})
            else:
                return redirect(reverse('twitter_app:home', args=(user_id,)))
