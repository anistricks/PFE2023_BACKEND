# Generated by Django 4.1.4 on 2023-12-11 12:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('commandesApp', '0001_initial'),
        ('livraisonsApp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='livraison',
            name='commande',
        ),
        migrations.AddField(
            model_name='livraison',
            name='commandes',
            field=models.ManyToManyField(to='commandesApp.commande'),
        ),
    ]
