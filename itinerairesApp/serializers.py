from rest_framework import serializers
from .models import Itineraire
from commandesApp.serializers import CommandeSerializer
from usersApp.serializers import UserSerializer

class ItineraireSerializer(serializers.ModelSerializer):
    commandes = CommandeSerializer(many=True, read_only=True)
    livreur = UserSerializer()

    class Meta:
        model = Itineraire
        fields = ['id', 'commandes', 'livreur', 'status']
