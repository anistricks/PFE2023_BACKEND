from rest_framework import serializers
from .models import Livraison, LigneLivraison
from clientsApp.serializers import ClientSerializer
from usersApp.serializers import UserSerializer
from articlesApp.serializers import ArticleSerializer
from articlesApp.models import Article
from clientsApp.models import Client

class LigneLivraisonSerializer(serializers.ModelSerializer):
    article = serializers.PrimaryKeyRelatedField(queryset=Article.objects.all())

    class Meta:
        model = LigneLivraison
        fields = ['article', 'quantite','isModified']

class LivraisonSerializer(serializers.ModelSerializer):
    client = serializers.PrimaryKeyRelatedField(queryset=Client.objects.all())
    lignes_livraison = LigneLivraisonSerializer(many=True, read_only=True)

    class Meta:
        model = Livraison
        fields = ['id', 'client', 'date_livraison', 'status','isModified', 'lignes_livraison']
