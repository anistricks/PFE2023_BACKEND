# Generated by Django 4.1.4 on 2023-12-12 10:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('livraisonsApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='lignelivraison',
            name='isModified',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='livraison',
            name='isModified',
            field=models.BooleanField(default=False),
        ),
    ]