from django.contrib import admin
from todo_app import models as django_models

# Register your models here.

# admin.site.site_header = '1111111111'  # default: "Django Administration"
# admin.site.index_title = '22222222222'  # default: "Site administration"
# admin.site.site_title = '333333333'  # default: "Django site admin"



class Tasks(admin.ModelAdmin):
    """
        Settings admin page for Todo
    """
    list_display = (  # отображение
        'id',
        'task_title',
        'done',
    )
    list_display_links = (  # для ссылка (для перехода внутрь)
        'id',
        'task_title',
        'done',
    )
    list_editable = (  # поле, доступное для редактирования в общем списке

    )
    list_filter = (  # поля для фильтрации
        'id',
        'task_title',
        'done',
    )
    search_fields = (  # поля для поиска (ввод поиска в одном месте)
        'id',
        'task_title',
        'done',
    )
    fieldsets = (
        # ("ID", {"fields": ('id',)}),
        ("Title", {"fields": ('task_title',)}),
        ("Done", {"fields": ('done',)}),
    )


admin.site.register(django_models.Tasks, Tasks)  # complex register model