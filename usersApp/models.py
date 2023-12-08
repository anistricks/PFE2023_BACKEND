from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=20,unique=True)
    password = models.CharField(max_length=255, default='TO_BE_SET') 
    isAdmin = models.BooleanField(default=False)

    def __str__(self):
        return self.username