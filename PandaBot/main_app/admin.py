from django.contrib import admin
from main_app import models as django_models


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
        'user_name',
        'token',
    )
    list_display_links = (  # для ссылка (для перехода внутрь)
        'id',
        'user_name',
        'token',
    )
    list_editable = (  # поле, доступное для редактирования в общем списке

    )
    list_filter = (  # поля для фильтрации
        'id',
        'user_name',
        'token',
    )
    search_fields = (  # поля для поиска (ввод поиска в одном месте)
        'id',
        'user_name',
        'token',
    )
    fieldsets = (
        # ("ID", {"fields": ('id',)}),
        ("ID", {"fields": ('id',)}),
        ("Nickname", {"fields": ('user_name',)}),
        ("Password", {"fields": ('token',)}),
    )


admin.site.register(django_models.Users, Users)  # complex register model
