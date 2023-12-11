from django.db import models

# Create your models here.

class Article(models.Model):
    nom = models.CharField(max_length=100,unique=True,blank=False, null=False)

    def __str__(self):
        return self.nom