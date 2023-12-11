from rest_framework import serializers
from .models import Livraison
from commandesApp.serializers import CommandeSerializer
from usersApp.serializers import UserSerializer

class LivraisonSerializer(serializers.ModelSerializer):
    commandes = CommandeSerializer(many=True, read_only=True)
    livreur = UserSerializer()

    class Meta:
        model = Livraison
        fields = ['id', 'commandes', 'livreur', 'status']
