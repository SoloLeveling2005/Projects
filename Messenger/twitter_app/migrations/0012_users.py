# Generated by Django 4.1.3 on 2022-11-24 04:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('twitter_app', '0011_alter_tweets_parent_tweet_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('user_name', models.CharField(blank=True, default='', max_length=300, verbose_name='user_name')),
                ('user_nickname', models.CharField(blank=True, default='', max_length=300, verbose_name='user_nickname')),
                ('user_password', models.CharField(blank=True, default='', max_length=300, verbose_name='user_password')),
                ('user_profile_description', models.CharField(blank=True, default='', max_length=500, verbose_name='user_profile_description')),
                ('user_following', models.IntegerField(blank=True, default=0, verbose_name='user_following')),
                ('user_followers', models.IntegerField(blank=True, default=0, verbose_name='user_followers')),
                ('user_tweet_quantity', models.IntegerField(blank=True, default=0, verbose_name='user_followers')),
            ],
            options={
                'verbose_name': 'Пользователь',
                'verbose_name_plural': 'Пользователи',
                'ordering': ('id',),
            },
        ),
    ]
