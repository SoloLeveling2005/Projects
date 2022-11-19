from django.contrib import admin
from log_auth import models as django_models


class Users(admin.ModelAdmin):
    """
    Settings admin page for Todo
    """
    list_display = (  # отображение
        'id',
        'user_nickname',
        'user_password'
    )
    list_display_links = (  # для ссылка (для перехода внутрь)
        'id',
        'user_nickname',
        'user_password'
    )
    list_editable = (  # поле, доступное для редактирования в общем списке

    )
    list_filter = (  # поля для фильтрации
        'id',
        'user_nickname',
        'user_password'
    )
    search_fields = (  # поля для поиска (ввод поиска в одном месте)
        'id',
        'user_nickname',
        'user_password'
    )
    fieldsets = (
        # ("ID", {"fields": ('id',)}),
        ("nickname", {"fields": ('user_nickname',)}),
        ("password", {"fields": ('user_password',)}),
    )


admin.site.register(django_models.Users, Users)  # complex register model
