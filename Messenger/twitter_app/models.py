from django.db import models

# Create your models here.





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
