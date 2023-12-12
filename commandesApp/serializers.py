
from rest_framework import serializers
from .models import Commande, LigneCommande
from clientsApp.serializers import ClientSerializer
from usersApp.serializers import UserSerializer
from articlesApp.serializers import ArticleSerializer

class LigneCommandeSerializer(serializers.ModelSerializer):
    article = ArticleSerializer()

    class Meta:
        model = LigneCommande
        fields = ['article', 'quantite']

class CommandeSerializer(serializers.ModelSerializer):
    client = ClientSerializer()
    lignes_commande = LigneCommandeSerializer(many=True, read_only=True)

    class Meta:
        model = Commande
        fields = ['id', 'client', 'date_commande', 'lignes_commande']
