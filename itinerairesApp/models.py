from django.db import models
from usersApp.models import User
from clientsApp.models  import Client
from commandesApp.models  import Commande
class Itineraire(models.Model):
    clients = models.ManyToManyField(Client, blank=True)
    livreur = models.ForeignKey(User, on_delete=models.CASCADE)
    status_choices = [
        ('En attente', 'En attente'),
        ('En cours', 'En cours'),
        ('Fini', 'Fini'),
    ]
    status = models.CharField(max_length=20, choices=status_choices, default='En attente')
    commandes = models.ManyToManyField(Commande, blank=True)
    def __str__(self):
        return f"Itineraire - Statut: {self.status}"
