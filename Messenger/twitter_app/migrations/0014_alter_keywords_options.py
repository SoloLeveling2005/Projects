# Generated by Django 4.1.3 on 2022-11-27 03:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('twitter_app', '0013_keywords_rename_id_tweet_comments_tweet_id_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='keywords',
            options={'ordering': ('id',), 'verbose_name': 'Ключевое слово', 'verbose_name_plural': 'Ключевые слова'},
        ),
    ]