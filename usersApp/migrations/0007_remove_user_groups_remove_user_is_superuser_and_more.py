# Generated by Django 4.1.4 on 2023-12-11 20:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usersApp', '0006_user_groups_user_is_superuser_user_last_login_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='groups',
        ),
        migrations.RemoveField(
            model_name='user',
            name='is_superuser',
        ),
        migrations.RemoveField(
            model_name='user',
            name='user_permissions',
        ),
    ]