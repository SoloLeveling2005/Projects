from django.contrib import admin
from log_auth import models as django_models


class Users(admin.ModelAdmin):
    """
    Settings admin page for Todo
    """
    list_display = (  # отображение
        'id',
        'user_nickname',
        'user_password',
        'user_profile_description'
    )
    list_display_links = (  # для ссылка (для перехода внутрь)
        'id',
        'user_nickname',
        'user_password',
        'user_profile_description'
    )
    list_editable = (  # поле, доступное для редактирования в общем списке

    )
    list_filter = (  # поля для фильтрации
        'id',
        'user_nickname',
        'user_password',
        'user_profile_description'
    )
    search_fields = (  # поля для поиска (ввод поиска в одном месте)
        'id',
        'user_nickname',
        'user_password',
        'user_profile_description'
    )
    fieldsets = (
        # ("ID", {"fields": ('id',)}),
        ("Никнейм пользователя", {"fields": ('user_nickname',)}),
        ("Пароль пользователя", {"fields": ('user_password',)}),
        ("Описание профиля", {"fields": ('user_profile_description',)}),
    )


admin.site.register(django_models.Users, Users)  # complex register model
