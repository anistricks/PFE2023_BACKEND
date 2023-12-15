from rest_framework import serializers
from .models import Itineraire
from clientsApp.serializers import ClientSerializer  
from usersApp.models import User
from clientsApp.models import Client

class ItineraireSerializer(serializers.ModelSerializer):
    clients = ClientSerializer(many=True, read_only=True)
    clients_ids = serializers.PrimaryKeyRelatedField(
        many=True, 
        write_only=True, 
        queryset=Client.objects.all(), 
        source='clients',
        required=False
    )
    livreur = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), required=False)

    class Meta:
        model = Itineraire
        fields = ['id', 'clients', 'livreur', 'status', 'clients_ids']