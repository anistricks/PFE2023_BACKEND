from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=20,unique=True,blank=False, null=False)
    password = models.CharField(max_length=255,blank=False, null=False) 
    isAdmin = models.BooleanField(default=False)

    def __str__(self):
        return self.username