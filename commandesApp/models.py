# commandsApp/models.py
from django.db import models
from clientsApp.models import Client
from usersApp.models import User
from articlesApp.models import Article

class Commande(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    date_commande = models.DateTimeField(auto_now_add=True)

    #  status_choices = [
    #       ('En cours', 'En cours'),
    #       ('En préparation', 'En préparation'),
    #       ('Livré', 'Livré'),
    #   ]
    #   status = models.CharField(max_length=20, choices=status_choices, default='En cours')

    #nous avons fait en sorte que l'id de la commande soit égal à l'id du client qui la créée afin de facilité les appels au front.
    #forcer la valeur de l'id n'est pas recommandé.
    def save(self, *args, **kwargs):
        self.id = self.client.id
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Commande de {self.client.nom}"

    def __str__(self):
        return f"Commande de {self.client.nom} "
#- Statut: {self.status}
class LigneCommande(models.Model):
    commande = models.ForeignKey(Commande, on_delete=models.CASCADE)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    quantite = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.quantite} x {self.article.nom} dans la commande {self.commande.id}"
