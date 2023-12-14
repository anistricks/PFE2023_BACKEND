# Generated by Django 4.1.4 on 2023-12-14 18:01

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('livraisonsApp', '0004_lignelivraison_ismodified'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lignelivraison',
            name='quantite',
            field=models.FloatField(validators=[django.core.validators.MinValueValidator(0.0)]),
        ),
    ]