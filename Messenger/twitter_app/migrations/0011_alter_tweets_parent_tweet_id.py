# Generated by Django 4.1.3 on 2022-11-20 15:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('twitter_app', '0010_comments_alter_tweets_parent_tweet_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tweets',
            name='parent_tweet_id',
            field=models.IntegerField(blank=True, default=None, null=True, verbose_name='parent_tweet_id'),
        ),
    ]