import json
import re
from typing import Union

from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User, Group
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpRequest, HttpResponse, JsonResponse, HttpResponseBadRequest, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View
from random import randint
import datetime
import openpyxl
from openpyexcel.styles import Protection
from openpyxl.styles import colors
from openpyxl.styles import Font, Color
from openpyxl import Workbook

from django.views.decorators.csrf import csrf_exempt

from django_app.models import Products


# Create your views here.

def index(request: HttpRequest) -> HttpResponse:
    global NDS
    if request.method == "GET":
        data = list(Products.objects.all().values())
        for i in data:
            print(i)
            # {'id': 8, 'name': 'Ipad', 'quantity': '12', 'cost_without_cheat': '20000', 'cheat': '20', 'total_cost':
            # 288000, 'cost_with_VAT': 34560, 'total': 322560}
        filepath = "frontend/src/assets/exel/form.xlsx"
        wb = openpyxl.Workbook()
        font_all = Font(name='Montserrat', size=12, bold=True, )
        protection = openpyxl.styles.protection.Protection(locked=False, hidden=False)
        sheet = wb.active
        A1, B1, C1, D1, E1, F1, G1, H1 = sheet['A1'], sheet['B1'], sheet['C1'], sheet['D1'], sheet['E1'], sheet['F1'], \
                                         sheet['G1'], sheet['H1']
        A1.font = font_all
        B1.font = font_all
        C1.font = font_all
        D1.font = font_all
        E1.font = font_all
        F1.font = font_all
        G1.font = font_all
        H1.font = font_all
        A1.value = "id"
        B1.value = "наименование"
        C1.value = "количество"
        D1.value = "себестоимость"
        E1.value = "% накрутка"
        F1.value = "итоговая стоимость"
        G1.value = "стоимость НДС"
        H1.value = "итоговая"
        A = sheet.column_dimensions['A']
        B = sheet.column_dimensions['B']
        C = sheet.column_dimensions['C']
        D = sheet.column_dimensions['D']
        E = sheet.column_dimensions['E']
        F = sheet.column_dimensions['F']
        G = sheet.column_dimensions['G']
        H = sheet.column_dimensions['H']
        A.font = B.font = C.font = D.font = E.font = F.font = G.font = H.font = font_all
        B.protection = C.protection = D.protection = E.protection = protection
        A.width = 10
        B.width = C.width = D.width = E.width = F.width = G.width = H.width = 30
        sheet.protection.sheet = True
        sheet.protection.enable()
        sheet.protection.password = 'user2000'
        index = 2

        for mini_data in data:
            A_value = sheet[f'A{index}'].value = mini_data['id']
            B_value = sheet[f'B{index}'].value = " ".join(
                [str(mini_data['name'])[::-1][i:i + 3] for i in range(0, len(str(mini_data['name'])[::-1]), 3)])[::-1]
            C_value = sheet[f'C{index}'].value = " ".join([str(mini_data['quantity'])[::-1][i:i + 3] for i in
                                                           range(0, len(str(mini_data['quantity'])[::-1]), 3)])[::-1]
            D_value = sheet[f'D{index}'].value = " ".join([str(mini_data['cost_without_cheat'])[::-1][i:i + 3] for i in
                                                           range(0, len(str(mini_data['cost_without_cheat'])[::-1]),
                                                                 3)])[::-1]
            E_value = sheet[f'E{index}'].value = " ".join(
                [str(mini_data['cheat'])[::-1][i:i + 3] for i in range(0, len(str(mini_data['cheat'])[::-1]), 3)])[::-1]
            F_value = sheet[f'F{index}'].value = " ".join([str(mini_data['total_cost'])[::-1][i:i + 3] for i in
                                                           range(0, len(str(mini_data['total_cost'])[::-1]), 3)])[::-1]
            G_value = sheet[f'G{index}'].value = " ".join([str(mini_data['cost_with_VAT'])[::-1][i:i + 3] for i in
                                                           range(0, len(str(mini_data['cost_with_VAT'])[::-1]), 3)])[
                                                 ::-1]
            H_value = sheet[f'H{index}'].value = " ".join(
                [str(mini_data['total'])[::-1][i:i + 3] for i in range(0, len(str(mini_data['total'])[::-1]), 3)])[::-1]
            sheet[f'B{index}'].protection = protection
            sheet[f'C{index}'].protection = protection
            sheet[f'D{index}'].protection = protection
            sheet[f'E{index}'].protection = protection
            index += 1
        wb.save(filepath)

        return render(request, 'index.html',
                      context={'datas': data})
    elif request.method == "POST":

        try:
            excel_file = request.FILES["excel_file"]
            wb = openpyxl.load_workbook(excel_file)
            sheet = wb.active
            index = 2
            NDS = 12

            while True:
                A_value = str(sheet[f'A{index}'].value).replace(' ', '')
                B_value = str(sheet[f'B{index}'].value).replace(' ', '')
                C_value = str(sheet[f'C{index}'].value).replace(' ', '')
                D_value = str(sheet[f'D{index}'].value).replace(' ', '')
                E_value = str(sheet[f'E{index}'].value).replace(' ', '')
                F_value = str(sheet[f'F{index}'].value).replace(' ', '')
                G_value = str(sheet[f'G{index}'].value).replace(' ', '')
                H_value = str(sheet[f'H{index}'].value).replace(' ', '')
                if any(x is None for x in (B_value, C_value, D_value, E_value, F_value, G_value, H_value)):
                    break
                total_cost = int(C_value) * (
                        int(D_value) + int(int(D_value) / 100) * int(E_value))
                cost_with_VAT = total_cost * NDS / 100
                total = total_cost + cost_with_VAT
                if A_value is None or A_value == "None":
                    print("Создание")
                    # NDS = 12
                    # Значит это новая запись
                    # {'id': 8, 'name': 'Ipad', 'quantity': '12', 'cost_without_cheat': '20000', 'cheat': '20', 'total_cost': 288000, 'cost_with_VAT': 34560, 'total': 322560}



                    Products.objects.create(name=B_value, quantity=C_value,
                                            cost_without_cheat=D_value,
                                            cheat=E_value, total_cost=total_cost, cost_with_VAT=cost_with_VAT,
                                            total=total)
                else:
                    print("Замена")
                    print(A_value)
                    # Иначе, сравнивание и перезапись
                    data = Products.objects.get(id=A_value)
                    if (data.name != B_value):
                        data.name = B_value
                        data.save()
                    if (data.quantity != C_value):
                        data.quantity = C_value
                        data.save()
                    if (data.cost_without_cheat != D_value):
                        data.cost_without_cheat = D_value
                        data.save()
                    if (data.cheat != E_value):
                        data.cheat = E_value
                        data.save()
                    if (data.total_cost != F_value):
                        data.total_cost = total_cost
                        data.save()
                    if (data.cost_with_VAT != G_value):
                        data.cost_with_VAT = cost_with_VAT
                        data.save()
                    if (data.total != H_value):
                        data.total = total
                        data.save()
                print([A_value, B_value, C_value, D_value, E_value, F_value, G_value, H_value])
                index += 1


        except Exception as e:
            print(e)
            id = request.POST.get(f'id', "")
            id_name = request.POST.get(f'name', "").replace(' ', '')
            id_quantity = request.POST.get(f'quantity', "").replace(' ', '')
            id_cost_without_cheat = request.POST.get(f'cost_without_cheat', "").replace(' ', '')
            id_cheat = request.POST.get(f'cheat', "").replace(' ', '')
            NDS = 12
            print(id)
            print(id_cheat)
            if id_name == "" or id_quantity == "" or id_cost_without_cheat == "" or id_cheat == "":
                return redirect(reverse('django_app:index', args=()))
            else:
                try:
                    data = Products.objects.get(id=id)
                    id_name_db = Products.objects.get(id=id).name
                    id_quantity_db = Products.objects.get(id=id).quantity
                    id_cost_without_cheat_db = Products.objects.get(id=id).cost_without_cheat
                    id_cheat_db = Products.objects.get(id=id).cheat
                    id_total_cost_db = Products.objects.get(id=id).total_cost
                    id_cost_with_VAT_db = Products.objects.get(id=id).cost_with_VAT
                    id_total_db = Products.objects.get(id=id).total
                    empty = False

                    if id_name != id_name_db:
                        data.name = id_name
                        data.save()
                    if id_quantity != id_quantity_db:
                        data.quantity = id_quantity
                        data.save()
                        empty = True

                    if id_cost_without_cheat != id_cost_without_cheat_db:
                        data.cost_without_cheat = id_cost_without_cheat
                        data.save()
                        empty = True
                    if id_cheat != id_cheat_db:
                        data.cheat = id_cheat
                        data.save()
                        empty = True
                    '''
                        let money = +quantity * (+cost_without_cheat + Number(+cost_without_cheat/100)*cheat)
                        let money_with_nds = money * NDS / 100
        
                        document.querySelector(`#total_cost${code}`).value = money
                        document.querySelector(`#cost_with_VAT${code}`).value = money_with_nds
                        document.querySelector(`#total${code}`).value = money + money_with_nds
                    '''
                    if empty:
                        total_cost = int(id_quantity_db) * (
                                int(id_cost_without_cheat) + int(int(id_cost_without_cheat) / 100) * int(id_cheat))
                        cost_with_VAT = total_cost * NDS / 100
                        total = total_cost + cost_with_VAT

                        data.total_cost = total_cost
                        data.save()
                        data.cost_with_VAT = cost_with_VAT
                        data.save()
                        data.total = total
                        data.save()
                except Exception as e:
                    print(e)
                    total_cost = int(id_quantity) * (
                            int(id_cost_without_cheat) + int(int(id_cost_without_cheat) / 100) * int(id_cheat))
                    cost_with_VAT = total_cost * NDS / 100
                    total = total_cost + cost_with_VAT

                    Products.objects.create(name=id_name, quantity=id_quantity,
                                            cost_without_cheat=id_cost_without_cheat,
                                            cheat=id_cheat, total_cost=total_cost, cost_with_VAT=cost_with_VAT,
                                            total=total)
        return redirect(reverse('django_app:index', args=()))
