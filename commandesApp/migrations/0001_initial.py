# Generated by Django 4.1.4 on 2023-12-10 11:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('clientsApp', '0003_alter_client_nom'),
        ('articlesApp', '0001_initial'),
        ('usersApp', '0003_alter_user_username'),
    ]

    operations = [
        migrations.CreateModel(
            name='Commande',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_commande', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(choices=[('En cours', 'En cours'), ('En préparation', 'En préparation'), ('Livré', 'Livré')], default='En cours', max_length=20)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clientsApp.client')),
                ('livreur', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='usersApp.user')),
            ],
        ),
        migrations.CreateModel(
            name='LigneCommande',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantite', models.PositiveIntegerField()),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='articlesApp.article')),
                ('commande', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='commandesApp.commande')),
            ],
        ),
    ]
