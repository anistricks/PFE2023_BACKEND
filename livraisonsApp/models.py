from django.db import models
from clientsApp.models import Client
from django.core.validators import MinValueValidator
from articlesApp.models import Article

class Livraison(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    date_livraison = models.DateTimeField(auto_now_add=True)
    status_choices = [
        ('En cours', 'En cours'),
        ('En préparation', 'En préparation'),
        ('Livrée', 'Livrée'),
    ]
    status = models.CharField(max_length=20, choices=status_choices, default='En cours')
    isModified = models.BooleanField(default=False)

    def __str__(self):
        return f"Livraison pour {self.client.nom} - Statut: {self.status}"

class LigneLivraison(models.Model):
    livraison = models.ForeignKey(Livraison, on_delete=models.CASCADE)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    quantite = models.FloatField(validators=[MinValueValidator(0.0)])
    isModified = models.BooleanField(default=False)
    

    def __str__(self):
        return f"{self.quantite} x {self.article.nom} dans la livraison {self.livraison.id}"
