from django.shortcuts import render
from rest_framework import status, permissions
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response

from api import models
from api import serializers as django_serializers

# Create your views here.


@api_view(http_method_names=["POST", "GET", "DELETE"])
@permission_classes((permissions.AllowAny,))
def get_sites(request):
    print("index")
    if request.method == "GET":
        try:
            data = models.Site.objects.all()
            data_json = django_serializers.SitesSerializer(instance=data, many=True).data
            return Response(data=data_json, status=status.HTTP_200_OK)
        except:
            return Response(status=401)
