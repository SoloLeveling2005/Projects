from django.http import HttpResponse
from django.shortcuts import render, redirect

from messenger import models


# Create your views here.


def index(request):
    user_id_cookie = request.COOKIES.get('username')
    if user_id_cookie is not None:
        rooms = models.Room.objects.all()
        user = models.User.objects.get(name=user_id_cookie)
        print("user.id", user.id)
        # room = models.Room.objects.get(slug=1)
        # messages = models.Message.objects.filter(room=room)
        response = render(request, "index.html", context={"rooms": rooms,
                                                          # "messages": messages,
                                                          "username": user_id_cookie,
                                                          "user_id": user.id})
        return response
    else:
        return redirect('auth')


def auth(request):
    if request.method == 'GET':
        user_id_cookie = request.COOKIES.get('username')
        if user_id_cookie is not None:
            return redirect('index')
        else:
            print("None")
            response = render(request, "identification.html", context={})
            return response

    elif request.method == 'POST':
        username = request.POST.get('username')
        # password = request.POST.get('password')
        try:
            user = models.User.objects.get(name=username)
            response = render(request, "identification.html", context={})
            return response
        except Exception as e:
            print(e)
            models.User.objects.create(name=username)
            response = redirect('index')
            response.set_cookie('username', username)

            return response
