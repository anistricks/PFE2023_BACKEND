# livraisonsApp/models.py
from django.db import models
from commandesApp.models import Commande
from usersApp.models import User

class Livraison(models.Model):
    STATUT_CHOICES = [
        ('En attente', 'En attente'),
        ('En cours', 'En cours'),
        ('Fini', 'Fini'),
    ]

    commande = models.ForeignKey(Commande, on_delete=models.CASCADE)
    livreur = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=STATUT_CHOICES, default='En attente')

    def __str__(self):
        return f"Livraison de la commande {self.commande.id} - Statut: {self.status}"
