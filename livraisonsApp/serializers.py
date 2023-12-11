from rest_framework import serializers
from .models import Livraison
from commandesApp.serializers import CommandeSerializer
from usersApp.serializers import UserSerializer

class LivraisonSerializer(serializers.ModelSerializer):
    commande = CommandeSerializer()
    livreur = UserSerializer()

    class Meta:
        model = Livraison
        fields = ['id', 'commande', 'livreur', 'status']
