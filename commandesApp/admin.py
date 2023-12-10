from django.contrib import admin
from .models import Commande
from .models import LigneCommande
# Register your models here.
admin.site.register(Commande)
admin.site.register(LigneCommande)