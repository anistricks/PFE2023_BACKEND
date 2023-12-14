
from django.db import models
from clientsApp.models import Client
from django.core.validators import MinValueValidator
from articlesApp.models import Article

class Commande(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    date_commande = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        self.id = self.client.id
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Commande de {self.client.nom}"

    def __str__(self):
        return f"Commande de {self.client.nom} "

class LigneCommande(models.Model):
    commande = models.ForeignKey(Commande, on_delete=models.CASCADE)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    quantite = models.FloatField(validators=[MinValueValidator(0.0)])

    def __str__(self):
        return f"{self.quantite} x {self.article.nom} dans la commande {self.commande.id}"
