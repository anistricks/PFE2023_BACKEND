# Generated by Django 4.1.4 on 2023-12-11 08:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clientsApp', '0004_alter_client_adresse_complete'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='adresse_complete',
            field=models.CharField(max_length=255),
        ),
    ]