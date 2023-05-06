from django.contrib import admin
from twitter_app import models as django_models


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
        'user_nickname',
        'user_password',
        'user_profile_description',
        'user_following',
        'user_followers',
        'user_tweet_quantity'
    )
    list_display_links = (  # для ссылка (для перехода внутрь)
        'id',
        'user_name',
        'user_nickname',
        'user_password',
        'user_profile_description',
        'user_following',
        'user_followers',
        'user_tweet_quantity'
    )
    list_editable = (  # поле, доступное для редактирования в общем списке

    )
    list_filter = (  # поля для фильтрации
        'id',
        'user_name',
        'user_nickname',
        'user_password',
        'user_profile_description',
        'user_following',
        'user_followers',
        'user_tweet_quantity'
    )
    search_fields = (  # поля для поиска (ввод поиска в одном месте)
        'id',
        'user_name',
        'user_nickname',
        'user_password',
        'user_profile_description',
        'user_following',
        'user_followers',
        'user_tweet_quantity'
    )
    fieldsets = (
        # ("ID", {"fields": ('id',)}),
        ("Имя", {"fields": ('user_name',)}),
        ("Никнейм", {"fields": ('user_nickname',)}),
        ("Пароль", {"fields": ('user_password',)}),
        ("Описание профиля", {"fields": ('user_profile_description',)}),
        ("Подписки", {"fields": ('user_following',)}),
        ("Подписчики", {"fields": ('user_followers',)}),
        ("Кол-во твитов", {"fields": ('user_tweet_quantity',)}),
    )


class Tweets(admin.ModelAdmin):
    """
        Settings admin page for Todo
    """
    list_display = (  # отображение
        'id',
        'author_id',
        'author_nickname',
        'tweet_text',
        'likes',
        'comments',
        'parent_tweet_id',
    )
    list_display_links = (  # для ссылка (для перехода внутрь)
        'id',
        'author_id',
        'author_nickname',
        'tweet_text',
        'likes',
        'comments',
        'parent_tweet_id',
    )
    list_editable = (  # поле, доступное для редактирования в общем списке

    )
    list_filter = (  # поля для фильтрации
        'id',
        'author_id',
        'author_nickname',
        'tweet_text',
        'likes',
        'comments',
        'parent_tweet_id',
    )
    search_fields = (  # поля для поиска (ввод поиска в одном месте)
        'id',
        'author_id',
        'author_nickname',
        'tweet_text',
        'likes',
        'comments',
        'parent_tweet_id',
    )
    fieldsets = (
        # ("Id поста", {"fields": ('id_tweet',)}),
        ("ID автора", {"fields": ('author_id',)}),
        ("Никнейм автора", {"fields": ('author_nickname',)}),
        ("Текст", {"fields": ('tweet_text',)}),
        ("Кол-во лайков", {"fields": ('likes',)}),
        ("Кол-во комментариев", {"fields": ('comments',)}),
        ("Родитель твита", {"fields": ('parent_tweet_id',)}),
    )


class Rating(admin.ModelAdmin):
    """
        Settings admin page for Todo
    """
    list_display = (  # отображение
        'id',
        'tweet_id',
        'user_id',
    )
    list_display_links = (  # для ссылка (для перехода внутрь)
        'id',
        'tweet_id',
        'user_id',
    )
    list_editable = (  # поле, доступное для редактирования в общем списке

    )
    list_filter = (  # поля для фильтрации
        'id',
        'tweet_id',
        'user_id',
    )
    search_fields = (  # поля для поиска (ввод поиска в одном месте)
        'id',
        'tweet_id',
        'user_id',
    )
    fieldsets = (
        # ("Id поста", {"fields": ('id_tweet',)}),
        ("ID твита", {"fields": ('tweet_id',)}),
        ("ID автора", {"fields": ('user_id',)}),
    )


class Comments(admin.ModelAdmin):
    """
        Settings admin page for Todo
    """
    list_display = (  # отображение
        'id',
        'tweet_id',
        'user_id',
    )
    list_display_links = (  # для ссылка (для перехода внутрь)
        'id',
        'tweet_id',
        'user_id',
    )
    list_editable = (  # поле, доступное для редактирования в общем списке

    )
    list_filter = (  # поля для фильтрации
        'id',
        'tweet_id',
        'user_id',
    )
    search_fields = (  # поля для поиска (ввод поиска в одном месте)
        'id',
        'tweet_id',
        'user_id',
    )
    fieldsets = (
        # ("Id поста", {"fields": ('id_tweet',)}),
        ("ID твита", {"fields": ('tweet_id',)}),
        ("ID автора", {"fields": ('user_id',)}),
    )


class Keywords(admin.ModelAdmin):
    """
        Settings admin page for Todo
    """
    list_display = (  # отображение
        'id',
        'tweet_id',
        'keyword',
    )
    list_display_links = (  # для ссылка (для перехода внутрь)
        'id',
        'tweet_id',
        'keyword',
    )
    list_editable = (  # поле, доступное для редактирования в общем списке

    )
    list_filter = (  # поля для фильтрации
        'id',
        'tweet_id',
        'keyword',
    )
    search_fields = (  # поля для поиска (ввод поиска в одном месте)
        'id',
        'tweet_id',
        'keyword',
    )
    fieldsets = (
        ("ID твита", {"fields": ('tweet_id',)}),
        ("Ключевое слово", {"fields": ('keyword',)}),
    )




admin.site.register(django_models.Users, Users)  # complex register model
admin.site.register(django_models.Tweets, Tweets)  # complex register model
admin.site.register(django_models.Rating, Rating)  # complex register model
admin.site.register(django_models.Comments, Comments)  # complex register model
admin.site.register(django_models.Keywords, Keywords)  # complex register model
