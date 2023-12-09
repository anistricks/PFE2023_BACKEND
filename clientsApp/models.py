from django.db import models

# Create your models here.
from django.db import models

class Client(models.Model):
    nom = models.CharField(max_length=100,unique=True)
    adresse_complete = models.CharField(max_length=255, default='valeur_par_defaut')

    def __str__(self):
        return f"{self.nom} - {self.adresse_complete}"
