from django.db import models


# Create your models here.


class Users(models.Model):
    id = models.AutoField(primary_key=True)
    list_display_links = None
    # list_editable = ['nickname', 'password']
    user_name = models.CharField(  #
        verbose_name="user_name",
        default="",
        editable=True,
        blank=True,

        max_length=300
    )
    user_nickname = models.CharField(  #
        verbose_name="user_nickname",
        default="",
        editable=True,
        blank=True,

        max_length=300
    )
    user_password = models.CharField(  #
        verbose_name="user_password",
        default="",
        editable=True,
        blank=True,

        max_length=300
    )
    user_profile_description = models.CharField(  #
        verbose_name="user_profile_description",
        default="",
        editable=True,
        blank=True,

        max_length=500
    )
    user_following = models.IntegerField(  # сколько у пользователя подписок на кого либо
        verbose_name="user_following",
        default=0,
        editable=True,
        blank=True,
    )
    user_followers = models.IntegerField(  # сколько у пользователя подписчиков
        verbose_name="user_followers",
        default=0,
        editable=True,
        blank=True,
    )
    user_tweet_quantity = models.IntegerField(  # сколько у пользователя опубликованных твитов
        verbose_name="user_followers",
        default=0,
        editable=True,
        blank=True,
    )

    class Meta:
        app_label = 'twitter_app'
        ordering = ('id',)
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
        # db_table

    # def __str__(self):
    #     return f"Todo: {self.title} ({self.user}) [{self.id}]"


class Tweets(models.Model):  # TODO таблица в базе данных
    id = models.AutoField(primary_key=True)
    list_display_links = None
    # list_editable = ['nickname', 'password']
    id_tweet = models.IntegerField(
        verbose_name="id_tweet",
        default=0,
        editable=True,
        blank=True,
    )

    author_id = models.IntegerField(
        verbose_name="author_id",
        default=0,
        editable=True,
        blank=True,

    )
    author_nickname = models.CharField(
        verbose_name="author_nickname",
        default="",
        editable=True,
        blank=True,
        max_length=300
    )
    text_tweet = models.CharField(
        verbose_name="text_tweet",
        default="",
        editable=True,
        blank=True,
        max_length=300
    )
    likes = models.IntegerField(
        verbose_name="likes",
        default=0,
        editable=True,
        blank=True,
    )
    comments = models.IntegerField(
        verbose_name="comments",
        default=0,
        editable=True,
        blank=True,
    )
    parent_tweet_id = models.IntegerField(
        verbose_name="parent_tweet_id",
        default=None,
        editable=True,
        blank=True,
        null=True
    )

    class Meta:
        app_label = 'twitter_app'
        ordering = ('id',)
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'
        # db_table


class Rating(models.Model):  # TODO таблица в базе данных
    id = models.AutoField(primary_key=True)
    list_display_links = None

    id_tweet = models.IntegerField(  # TODO поле в этой таблице
        verbose_name="id_tweet",
        default=0,
        editable=True,
        blank=True,
    )

    user_id = models.IntegerField(  # TODO поле в этой таблице
        verbose_name="user_id",
        default=0,
        editable=True,
        blank=True,

    )

    class Meta:
        app_label = 'twitter_app'
        ordering = ('id',)
        verbose_name = 'Рейтинг твита'
        verbose_name_plural = 'Рейтинг твитов'
        # db_table


class Comments(models.Model):
    id = models.AutoField(primary_key=True)
    list_display_links = None

    id_tweet = models.IntegerField(
        verbose_name="id_tweet",
        default=0,
        editable=True,
        blank=True,
    )

    user_id = models.IntegerField(
        verbose_name="user_id",
        default=0,
        editable=True,
        blank=True,
    )

    class Meta:
        app_label = 'twitter_app'
        ordering = ('id',)
        verbose_name = 'Комментарии твита'
        verbose_name_plural = 'Комментарии твитов'
        # db_table
