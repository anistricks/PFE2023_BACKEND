from rest_framework import serializers
from .models import Livraison, LigneLivraison
from clientsApp.serializers import ClientSerializer
from usersApp.serializers import UserSerializer
from articlesApp.serializers import ArticleSerializer

class LigneLivraisonSerializer(serializers.ModelSerializer):
    article = ArticleSerializer()

    class Meta:
        model = LigneLivraison
        fields = ['article', 'quantite']

class LivraisonSerializer(serializers.ModelSerializer):
    client = ClientSerializer()
    lignes_livraison = LigneLivraisonSerializer(many=True, read_only=True)

    class Meta:
        model = Livraison
        fields = ['id', 'client', 'date_livraison', 'status', 'lignes_livraison']
