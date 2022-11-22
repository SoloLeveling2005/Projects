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
    user_profile_description = models.CharField(
        verbose_name="user_profile_description",
        default="",
        editable=True,
        blank=True,

        max_length=300  # TODO свойство(параметр) этого поля
    )

    class Meta:
        app_label = 'log_auth'
        ordering = ('id',)
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
        # db_table

    # def __str__(self):
    #     return f"Todo: {self.title} ({self.user}) [{self.id}]"
