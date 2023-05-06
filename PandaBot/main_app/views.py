import datetime
import random

import bcrypt
from django.shortcuts import render

from main_app.models import Users


# Create your views here.

def identification(request):
    print(request.method)
    if request.method == "GET":
        return render(request, 'identification.html', context={"error": ""})

    elif request.method == "POST":
        salt = bcrypt.gensalt()

        id_ = (str(datetime.datetime.now()) + str(random.randint(100, 999))).encode("utf-8")

        token1 = request.POST.get('token1').encode("utf-8")
        token2 = request.POST.get('token2').encode("utf-8")
        token3 = request.POST.get('token3').encode("utf-8")

        id_ = bcrypt.hashpw(id_, salt)
        token1 = bcrypt.hashpw(token1, salt)
        token2 = bcrypt.hashpw(token2, salt)
        token3 = bcrypt.hashpw(token3, salt)

        # if bcrypt.checkpw(token, hashed):
        #     print("Password match.")
        # else:
        #     print("Password doesn't match.")
        Users.objects.create(id_=id_, token1=token1, token2=token2, token3=token3)
        response = render(request, 'home.html', context={})
        response.set_cookie('id_', id_)
        return response
