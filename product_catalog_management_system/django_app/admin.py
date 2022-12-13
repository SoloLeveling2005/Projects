from django.contrib import admin
from django_app import models as django_models


# Register your models here.

# admin.site.site_header = '1111111111'  # default: "Django Administration"
# admin.site.index_title = '22222222222'  # default: "Site administration"
# admin.site.site_title = '333333333'  # default: "Django site admin"


class Products(admin.ModelAdmin):
    list_display = (  # отображение
        'id',
        'name',
        'quantity',
        'cost_without_cheat',
        'cheat',
        'total_cost',
        'cost_with_VAT',
        'total'
    )
    list_display_links = (  # для ссылка (для перехода внутрь)
        'id',
        'name',
        'quantity',
        'cost_without_cheat',
        'cheat',
        'total_cost',
        'cost_with_VAT',
        'total'
    )
    list_editable = (  # поле, доступное для редактирования в общем списке

    )
    list_filter = (  # поля для фильтрации
        'id',
        'name',
        'quantity',
        'cost_without_cheat',
        'cheat',
        'total_cost',
        'cost_with_VAT',
        'total'
    )
    search_fields = (  # поля для поиска (ввод поиска в одном месте)
        'id',
        'name',
        'quantity',
        'cost_without_cheat',
        'cheat',
        'total_cost',
        'cost_with_VAT',
        'total'
    )
    fieldsets = (
        # ("ID", {"fields": ('id',)}),
        ("Имя", {"fields": ('name',)}),
        ("Количество", {"fields": ('quantity',)}),
        ("Стоимость без накрутки", {"fields": ('cost_without_cheat',)}),
        ("накрутка %", {"fields": ('cheat',)}),
        ("Итоговая стоимость", {"fields": ('total_cost',)}),
        ("Стоимость с НДС", {"fields": ('cost_with_VAT',)}),
        ("Итоговая", {"fields": ('total',)}),
    )

admin.site.register(django_models.Products, Products)  # complex register model