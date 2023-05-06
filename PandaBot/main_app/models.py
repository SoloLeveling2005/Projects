from django.db import models


# Create your models here.


class Users(models.Model):
    id = models.IntegerField(
        verbose_name="id_",
        default=0,
        editable=True,
        blank=True,
        primary_key=True
    )
    list_display_links = None
    # list_editable = ['nickname', 'password']
    user_name = models.CharField(  #
        verbose_name="user_name",
        default="Anonym",
        editable=True,
        blank=True,
        max_length=300,
    )
    token1 = models.CharField(  #
        verbose_name="token1",
        default="",
        editable=True,
        blank=True,
        max_length=300,
    )
    token2 = models.CharField(  #
        verbose_name="token1",
        default="",
        editable=True,
        blank=True,
        max_length=300,
    )
    token3 = models.CharField(  #
        verbose_name="token3",
        default="",
        editable=True,
        blank=True,
        max_length=300,
    )
    # user_nickname = models.CharField(  #
    #     verbose_name="user_nickname",
    #     default="",
    #     editable=True,
    #     blank=True,
    #
    #     max_length=300
    # )
    # user_password = models.CharField(  #
    #     verbose_name="user_password",
    #     default="",
    #     editable=True,
    #     blank=True,
    #
    #     max_length=300
    # )
    # user_profile_description = models.CharField(  #
    #     verbose_name="user_profile_description",
    #     default="",
    #     editable=True,
    #     blank=True,
    #
    #     max_length=500
    # )
    # user_following = models.IntegerField(  # сколько у пользователя подписок на кого либо
    #     verbose_name="user_following",
    #     default=0,
    #     editable=True,
    #     blank=True,
    # )
    # user_followers = models.IntegerField(  # сколько у пользователя подписчиков
    #     verbose_name="user_followers",
    #     default=0,
    #     editable=True,
    #     blank=True,
    # )
    # user_tweet_quantity = models.IntegerField(  # сколько у пользователя опубликованных твитов
    #     verbose_name="user_followers",
    #     default=0,
    #     editable=True,
    #     blank=True,
    # )

    class Meta:
        app_label = 'main_app'
        ordering = ('id',)
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
        # db_table

    # def __str__(self):
    #     return f"Todo: {self.title} ({self.user}) [{self.id}]"
