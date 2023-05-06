import requests
from django.http import HttpRequest
from django.shortcuts import render
from rest_framework import permissions, status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response


@api_view(http_method_names=["GET", "PUT", "PATCH", "DELETE", "POST"])
@permission_classes((permissions.AllowAny,))
def test(request: HttpRequest, id_="0") -> Response:
    return Response(data={"detail": "Successfully do"}, status=status.HTTP_200_OK)


@api_view(http_method_names=["GET"])
@permission_classes((permissions.AllowAny,))
def supplier_stocks(request: HttpRequest, token: str, dateFrom: str) -> Response:
    "http://127.0.0.1:8000/api/supplier/stocks/token/eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJhY2Nlc3NJRCI6ImM2YjVhOWZjLWNkZDgtNGVlMS05N2E0LTA1OTg0YWU5OTI0YSJ9.yVjdq8vM3W3qO0WmVLsVh-KPYR1d_UT6uzApYydWCxo/dateFrom/2023-01-28"
    url = f"https://statistics-api.wildberries.ru/api/v1/supplier/stocks?dateFrom={dateFrom}"
    headers = {
        'accept': 'application/json',
        'Authorization': token
    }
    response = requests.get(url, headers=headers)
    data = []
    if response.status_code == 200:
        data = response.json()
        # for i in data:
        #     print(i)
        return Response(data={"detail": data, "len": len(data)}, status=status.HTTP_200_OK)
    elif response.status_code == 429:
        return Response(data={"error": f"Пользователь отправил слишком много запросов за последнее время: {response.status_code}"},
                        status=status.HTTP_204_NO_CONTENT)
    else:
        return Response(data={"error": f"Request failed with status code: {response.status_code}"},
                        status=status.HTTP_204_NO_CONTENT)



