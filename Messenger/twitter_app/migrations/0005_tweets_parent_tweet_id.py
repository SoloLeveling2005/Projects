# Generated by Django 4.1.1 on 2022-11-20 13:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('twitter_app', '0004_remove_rating_author_id_rating_user_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='tweets',
            name='parent_tweet_id',
            field=models.IntegerField(blank=True, default=None, verbose_name='parent_tweet'),
        ),
    ]