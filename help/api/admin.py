from django.contrib import admin
from api import models




class User(admin.ModelAdmin):
    """
    Настройки отображения, фильтрации и поиска модели:'Todo' на панели администратора
    """

    list_display = (
        'username',
        'gmail',
        'password',
        'created_at',
        'ico',
        'phone',
        'gender',
        'birthday'

    )
    list_display_links = (
        'username',
        'gmail',
        'password',
        'created_at',
        'ico',
        'phone',
        'gender',
        'birthday'
    )
    list_editable = (

    )
    list_filter = (
        'username',
        'gmail',
        'password',
        'created_at',
        'ico',
        'phone',
        'gender',
        'birthday'
    )
    fieldsets = (
        ('Основное', {'fields': (
            'username',
            'gmail',
            'password',
            'created_at',
            'ico',
            'phone',
            'gender',
            'birthday'
        )}),
    )
    search_fields = [
        'username',
        'gmail',
        'password',
        'created_at',
        'ico',
        'phone',
        'gender',
        'birthday'
    ]


class Site(admin.ModelAdmin):
    """
    Настройки отображения, фильтрации и поиска модели:'Todo' на панели администратора
    """

    list_display = (
        'ip',
        'title',
        'description',


    )
    list_display_links = (
        'ip',
        'title',
        'description',
    )
    list_editable = (

    )
    list_filter = (
        'ip',
        'title',
        'description',
    )
    fieldsets = (
        ('Основное', {'fields': (
            'ip',
            'title',
            'description',
        )}),
    )
    search_fields = [
        'ip',
        'title',
        'description',
    ]


admin.site.register(models.User, User)
admin.site.register(models.Site, Site)
