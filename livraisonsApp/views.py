from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Livraison, LigneLivraison
from .serializers import LivraisonSerializer, LigneLivraisonSerializer
from rest_framework.generics import ListAPIView
from rest_framework.exceptions import ValidationError
from articlesApp.models import Article
class LivraisonList(APIView):
    def get(self, request):
        livraisons = Livraison.objects.all()
        serializer = LivraisonSerializer(livraisons, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = LivraisonSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LivraisonDetail(APIView):
    def get_object(self, livraison_id):
        return get_object_or_404(Livraison, id=livraison_id)

    def get(self, request, livraison_id):
        livraison = self.get_object(livraison_id)
        serializer = LivraisonSerializer(livraison)
        return Response(serializer.data)

    def put(self, request, livraison_id):
        livraison = self.get_object(livraison_id)
        serializer = LivraisonSerializer(livraison, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, livraison_id):
        livraison = self.get_object(livraison_id)
        livraison.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class LigneLivraisonList(APIView):
    def get(self, request):
        lignes_livraison = LigneLivraison.objects.all()
        serializer = LigneLivraisonSerializer(lignes_livraison, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = LigneLivraisonSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LigneLivraisonDetail(APIView):
    def get_object(self, ligne_livraison_id):
        return get_object_or_404(LigneLivraison, id=ligne_livraison_id)

    def get(self, request, ligne_livraison_id):
        ligne_livraison = self.get_object(ligne_livraison_id)
        serializer = LigneLivraisonSerializer(ligne_livraison)
        return Response(serializer.data)

    def put(self, request, ligne_livraison_id):
        ligne_livraison = self.get_object(ligne_livraison_id)
        serializer = LigneLivraisonSerializer(ligne_livraison, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, ligne_livraison_id):
        ligne_livraison = self.get_object(ligne_livraison_id)
        ligne_livraison.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class ArticlesByLivraisonList(ListAPIView):
    serializer_class = LigneLivraisonSerializer

    def get_queryset(self):
        livraison_id = self.kwargs['livraison_id']
        return LigneLivraison.objects.filter(livraison__id=livraison_id)
    def post(self, request, livraison_id):
        lignes_data = request.data

        # Vérifier que les données sont une liste
        if not isinstance(lignes_data, list):
            raise ValidationError("Les données doivent être une liste d'articles.")

        created_records = []

        for ligne_data in lignes_data:
            article_id = ligne_data.get('article')
            quantite = ligne_data.get('quantite')

            if not article_id:
                raise ValidationError("L'article doit être spécifié avec un ID.")

            existing_record = LigneLivraison.objects.filter(livraison_id=livraison_id, article_id=article_id).first()

            if existing_record:
                raise ValidationError("L'article ID {} est déjà dans la liste de livraison. Veuillez modifier la quantité si nécessaire.".format(article_id))

            serializer = LigneLivraisonSerializer(data=ligne_data)
            if serializer.is_valid():
                created_record = serializer.save(livraison_id=livraison_id)
                created_records.append(created_record)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        return Response([LigneLivraisonSerializer(record).data for record in created_records], status=status.HTTP_201_CREATED)
    
    def put(self, request, livraison_id):
        article_id = request.data.get('article')
        quantite = request.data.get('quantite')

        if not article_id:
            raise ValidationError("L'article doit être spécifié avec un ID.")

        existing_record = LigneLivraison.objects.filter(livraison_id=livraison_id, article_id=article_id).first()

        if not existing_record:
            raise ValidationError("Cet article n'existe pas dans la liste de livraison.")

        serializer = LigneLivraisonSerializer(existing_record, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework import status
from .models import Livraison
from .serializers import LivraisonSerializer

class GetLivraisonByClientId(ListAPIView):
    serializer_class = LivraisonSerializer

    def get_queryset(self):
        client_id = self.kwargs['client_id']
        return Livraison.objects.filter(client__id=client_id)
