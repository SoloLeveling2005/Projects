# Generated by Django 4.1.3 on 2022-11-20 13:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('twitter_app', '0008_alter_tweets_parent_tweet_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='tweets',
            name='comments',
            field=models.IntegerField(blank=True, default=0, verbose_name='comments'),
        ),
    ]
