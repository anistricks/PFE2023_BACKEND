# Generated by Django 4.1.4 on 2023-12-11 08:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clientsApp', '0003_alter_client_nom'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='adresse_complete',
            field=models.CharField(default='', max_length=255),
        ),
    ]