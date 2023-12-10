# commandsApp/models.py
from django.db import models
from clientsApp.models import Client
from usersApp.models import User
from articlesApp.models import Article

class Commande(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    livreur = models.ForeignKey(User, on_delete=models.CASCADE)
    date_commande = models.DateTimeField(auto_now_add=True)
    status_choices = [
        ('En cours', 'En cours'),
        ('En préparation', 'En préparation'),
        ('Livré', 'Livré'),
    ]
    status = models.CharField(max_length=20, choices=status_choices, default='En cours')

    def __str__(self):
        return f"Commande de {self.client.nom} - Statut: {self.status}"

class LigneCommande(models.Model):
    commande = models.ForeignKey(Commande, on_delete=models.CASCADE)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    quantite = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.quantite} x {self.article.nom} dans la commande {self.commande.id}"
