# Generated by Django 4.1.3 on 2022-11-23 14:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('log_auth', '0002_users_user_profile_description'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Users',
        ),
    ]
