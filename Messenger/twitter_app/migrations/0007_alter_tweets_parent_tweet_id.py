# Generated by Django 4.1.1 on 2022-11-20 13:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('twitter_app', '0006_alter_tweets_parent_tweet_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tweets',
            name='parent_tweet_id',
            field=models.IntegerField(blank=True, default=-1, verbose_name='parent_tweet_id'),
        ),
    ]
