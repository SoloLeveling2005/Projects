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

    class Meta:
        app_label = 'twitter_app'
        ordering = ('id',)
        verbose_name = 'Пользователи'
        verbose_name_plural = 'Пользователи'
        # db_table

    # def __str__(self):
    #     return f"Todo: {self.title} ({self.user}) [{self.id}]"



class Tasks(models.Model):  # TODO таблица в базе данных
    id = models.AutoField(primary_key=True)
    list_display_links = None
    # list_editable = ['nickname', 'password']
    author_id = models.IntegerField(
        verbose_name="author_id",
        default=0,
        editable=True,
        blank=True,
    )
    title = models.CharField(  # TODO поле в этой таблице
        verbose_name="title",
        default="",
        editable=True,
        blank=True,
        max_length=300
    )
    description = models.CharField(  # TODO поле в этой таблице
        verbose_name="description",
        default="",
        editable=True,
        blank=True,
        max_length=300
    )

    class Meta:
        app_label = 'twitter_app'
        ordering = ('id',)
        verbose_name = 'Задачи'
        verbose_name_plural = 'Задачи'
        # db_table
