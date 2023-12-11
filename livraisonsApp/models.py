from django.db import models
from commandesApp.models import Commande
from usersApp.models import User

class Livraison(models.Model):
    commandes = models.ManyToManyField(Commande)
    livreur = models.ForeignKey(User, on_delete=models.CASCADE)
    status_choices = [
        ('En attente', 'En attente'),
        ('En cours', 'En cours'),
        ('Fini', 'Fini'),
    ]
    status = models.CharField(max_length=20, choices=status_choices, default='En attente')

    def __str__(self):
        return f"Livraison {self.id} - Statut: {self.status}"