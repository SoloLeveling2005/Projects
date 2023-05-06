from django.db import models


# Create your models here.
class Products(models.Model):
    id = models.AutoField(primary_key=True)
    list_display_links = None
    # name, quantity, cost without cheat, % cheat, total cost, cost with VAT, total
    name = models.CharField(  #
        verbose_name="name",
        default="",
        editable=True,
        blank=True,

        max_length=300
    )
    quantity = models.CharField(  #
        verbose_name="quantity",
        default="",
        editable=True,
        blank=True,

        max_length=300
    )
    cost_without_cheat = models.CharField(  #
        verbose_name="cost_without_cheat",
        default="",
        editable=True,
        blank=True,

        max_length=300
    )
    cheat = models.CharField(  #
        verbose_name="cheat",
        default="",
        editable=True,
        blank=True,

        max_length=500
    )
    total_cost = models.IntegerField(  # сколько у пользователя подписок на кого либо
        verbose_name="total_cost",
        default=0,
        editable=True,
        blank=True,
    )
    cost_with_VAT = models.IntegerField(  # сколько у пользователя подписчиков
        verbose_name="cost_with_VAT",
        default=0,
        editable=True,
        blank=True,
    )
    total = models.IntegerField(  # сколько у пользователя опубликованных твитов
        verbose_name="total",
        default=0,
        editable=True,
        blank=True,
    )

    class Meta:
        app_label = 'django_app'
        ordering = ('id',)
        verbose_name = 'product'
        verbose_name_plural = 'products'
        # db_table

    # def __str__(self):
    #     return f"Todo: {self.title} ({self.user}) [{self.id}]"


class Products(models.Model):
    id = models.AutoField(primary_key=True)
    list_display_links = None
    # name, quantity, cost without cheat, % cheat, total cost, cost with VAT, total
    name = models.CharField(  #
        verbose_name="name",
        default="",
        editable=True,
        blank=True,

        max_length=300
    )
    quantity = models.CharField(  #
        verbose_name="quantity",
        default="",
        editable=True,
        blank=True,

        max_length=300
    )
    cost_without_cheat = models.CharField(  #
        verbose_name="cost_without_cheat",
        default="",
        editable=True,
        blank=True,

        max_length=300
    )
    cheat = models.CharField(  #
        verbose_name="cheat",
        default="",
        editable=True,
        blank=True,

        max_length=500
    )
    total_cost = models.IntegerField(  # сколько у пользователя подписок на кого либо
        verbose_name="total_cost",
        default=0,
        editable=True,
        blank=True,
    )
    cost_with_VAT = models.IntegerField(  # сколько у пользователя подписчиков
        verbose_name="cost_with_VAT",
        default=0,
        editable=True,
        blank=True,
    )
    total = models.IntegerField(  # сколько у пользователя опубликованных твитов
        verbose_name="total",
        default=0,
        editable=True,
        blank=True,
    )

    class Meta:
        app_label = 'django_app'
        ordering = ('id',)
        verbose_name = 'product'
        verbose_name_plural = 'products'
        # db_table

    # def __str__(self):
    #     return f"Todo: {self.title} ({self.user}) [{self.id}]"
