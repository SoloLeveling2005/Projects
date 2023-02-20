
import json

from django.shortcuts import render
import requests
# Create your views here.
from django.http import HttpResponse, HttpRequest, JsonResponse
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from django.shortcuts import render
# from rest_framework.decorators import api_view, permission_classes
from rest_framework import permissions
# from django_app import serializers as django_serializers



def index(request):
    context = {}
    return render(request, "index.html", context=context)