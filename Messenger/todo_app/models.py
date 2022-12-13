from django.db import models

# Create your models here.






class Tasks(models.Model):  # TODO таблица в базе данных
    id = models.AutoField(primary_key=True)
    list_display_links = None
    # list_editable = ['nickname', 'password']

    task_title = models.CharField(  # TODO поле в этой таблице
        verbose_name="text_tweet",
        default="",
        editable=True,
        blank=True,
        max_length=300
    )
    done = models.BooleanField(
        verbose_name="done",
        default=False,
        editable=True,
        blank=True,
    )

    class Meta:
        app_label = 'todo_app'
        ordering = ('id',)
        verbose_name = 'Задачи'
        verbose_name_plural = 'Задачи'
        # db_table
