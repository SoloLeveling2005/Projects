# Generated by Django 4.1.1 on 2022-11-21 13:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('log_auth', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='users',
            name='user_profile_description',
            field=models.CharField(blank=True, default='', max_length=300, verbose_name='user_profile_description'),
        ),
    ]