from django.contrib import admin
from twitter_app import models as django_models

# Register your models here.

# admin.site.site_header = '1111111111'  # default: "Django Administration"
# admin.site.index_title = '22222222222'  # default: "Site administration"
# admin.site.site_title = '333333333'  # default: "Django site admin"


class Tweets(admin.ModelAdmin):
    """
        Settings admin page for Todo
    """
    list_display = (  # отображение
        'id',
        'author_id',
        'author_nickname',
        'text_tweet',
        'likes',
    )
    list_display_links = (  # для ссылка (для перехода внутрь)
        'id',
        'author_id',
        'author_nickname',
        'text_tweet',
        'likes',
    )
    list_editable = (  # поле, доступное для редактирования в общем списке

    )
    list_filter = (  # поля для фильтрации
        'id',
        'author_id',
        'author_nickname',
        'text_tweet',
        'likes',
    )
    search_fields = (  # поля для поиска (ввод поиска в одном месте)
        'id',
        'author_id',
        'author_nickname',
        'text_tweet',
        'likes',
    )
    fieldsets = (
        # ("Id поста", {"fields": ('id_tweet',)}),
        ("Id автора", {"fields": ('author_id',)}),
        ("Никнейм автора", {"fields": ('author_nickname',)}),
        ("Текст", {"fields": ('text_tweet',)}),
        ("Кол-во лайков", {"fields": ('likes',)}),
    )


admin.site.register(django_models.Tweets, Tweets)  # complex register model