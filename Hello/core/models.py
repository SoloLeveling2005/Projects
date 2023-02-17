from django.db import models


# Create your models here.
class User(models.Model):
    # id, title, description, price, date_add, status
    # id = models.CharField(max_length=)  # TODO это поле есть по-умолчанию (скрыто)
    # id = models.IntegerField()
    # title = models.CharField(max_length=100)
    # description = models.TextField()
    # price = models.IntegerField()
    # date_add = models.IntegerField()
    # status = models.BooleanField()
    # url_img = models.CharField(max_length=70)

    # todo обязательные

    username = models.CharField(max_length=100)
    gmail = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    created_at = models.CharField(max_length=100)

    # todo необязательные
    ico = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    gender = models.CharField(max_length=100)
    birthday = models.CharField(max_length=100)

    class Meta:
        app_label = 'core'
        ordering = ('id',)
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'


class Sites(models.Model):
    # todo необязательные
    ico = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    gender = models.CharField(max_length=100)
    birthday = models.CharField(max_length=100)

    class Meta:
        app_label = 'core'
        ordering = ('id',)
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
