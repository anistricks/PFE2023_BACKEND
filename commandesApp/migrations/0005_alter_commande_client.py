# Generated by Django 4.1.4 on 2023-12-13 08:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('clientsApp', '0005_alter_client_adresse_complete'),
        ('commandesApp', '0004_alter_commande_client'),
    ]

    operations = [
        migrations.AlterField(
            model_name='commande',
            name='client',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clientsApp.client'),
        ),
    ]
