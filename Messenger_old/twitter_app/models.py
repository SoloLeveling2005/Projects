from django.db import models

# Create your models here.



class Users(models.Model):  # TODO таблица в базе данных
    id = models.AutoField(primary_key=True)
    list_display_links = None
    # list_editable = ['nickname', 'password']
    user_nickname = models.CharField(  # TODO поле в этой таблице
        verbose_name="user_nickname",
        default="",
        editable=True,
        blank=True,

        max_length=300
    )
    user_password = models.CharField(
        verbose_name="user_password",
        default="",
        editable=True,
        blank=True,

        max_length=300  # TODO свойство(параметр) этого поля
    )
    user_id = models.IntegerField(
        verbose_name="unique_user_code",
        default=0,
        editable=True,
        blank=True,
    )

    class Meta:
        app_label = 'twitter_app'
        ordering = ('id',)
        verbose_name = 'Аккаунт'
        verbose_name_plural = 'Аккаунты'
        # db_table

    # def __str__(self):
    #     return f"Todo: {self.title} ({self.user}) [{self.id}]"



class Tweets(models.Model):  # TODO таблица в базе данных
    id = models.AutoField(primary_key=True)
    list_display_links = None
    # list_editable = ['nickname', 'password']
    id_tweet = models.IntegerField(  # TODO поле в этой таблице
        verbose_name="id_tweet",
        default=0,
        editable=True,
        blank=True,
    )

    author_id = models.IntegerField(  # TODO поле в этой таблице
        verbose_name="author_id",
        default=0,
        editable=True,
        blank=True,

    )
    author_nickname = models.CharField(  # TODO поле в этой таблице
        verbose_name="author_nickname",
        default="",
        editable=True,
        blank=True,
        max_length=300
    )
    text_tweet = models.CharField(  # TODO поле в этой таблице
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

    class Meta:
        app_label = 'twitter_app'
        ordering = ('id',)
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'
        # db_table
