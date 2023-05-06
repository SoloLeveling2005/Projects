from django.contrib import admin
from todo import models as django_models

# Register your models here.

# admin.site.site_header = '1111111111'  # default: "Django Administration"
# admin.site.index_title = '22222222222'  # default: "Site administration"
# admin.site.site_title = '333333333'  # default: "Django site admin"


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
        ("ID", {"fields": ('id',)}),
        ("Никнейм", {"fields": ('user_nickname',)}),
        ("Пароль", {"fields": ('user_password',)}),
    )

class Tasks(admin.ModelAdmin):
    """
        Settings admin page for Todo
    """
    list_display = (  # отображение
        'id',
        'author_id',
        'title',
        'description',
    )
    list_display_links = (  # для ссылка (для перехода внутрь)
        'id',
        'author_id',
        'title',
        'description',
    )
    list_editable = (  # поле, доступное для редактирования в общем списке

    )
    list_filter = (  # поля для фильтрации
        'id',
        'author_id',
        'title',
        'description',
    )
    search_fields = (  # поля для поиска (ввод поиска в одном месте)
        'id',
        'author_id',
        'title',
        'description',
    )
    fieldsets = (
        ("ID", {"fields": ('id',)}),
        ("ID автора", {"fields": ('author_id',)}),
        ("Текст задачи", {"fields": ('title',)}),
        ("Описание задачи", {"fields": ('description',)}),
    )


admin.site.register(django_models.Users, Users)  # complex register model
admin.site.register(django_models.Tasks, Tasks)  # complex register model