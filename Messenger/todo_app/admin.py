from django.contrib import admin
from todo_app import models as django_models

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
        ("nickname", {"fields": ('user_nickname',)}),
        ("password", {"fields": ('user_password',)}),
    )

class Tasks(admin.ModelAdmin):
    """
        Settings admin page for Todo
    """
    list_display = (  # отображение
        'id',
        'author_id',
        'task_title',
        'task_description',
        'done',
    )
    list_display_links = (  # для ссылка (для перехода внутрь)
        'id',
        'author_id',
        'task_title',
        'task_description',
        'done',
    )
    list_editable = (  # поле, доступное для редактирования в общем списке

    )
    list_filter = (  # поля для фильтрации
        'id',
        'author_id',
        'task_title',
        'task_description',
        'done',
    )
    search_fields = (  # поля для поиска (ввод поиска в одном месте)
        'id',
        'author_id',
        'task_title',
        'task_description',
        'done',
    )
    fieldsets = (
        ("ID", {"fields": ('id',)}),
        ("Author", {"fields": ('author_id',)}),
        ("Title", {"fields": ('task_title',)}),
        ("Description", {"fields": ('task_description',)}),
        ("Done", {"fields": ('done',)}),
    )


admin.site.register(django_models.Users, Users)  # complex register model
admin.site.register(django_models.Tasks, Tasks)  # complex register model