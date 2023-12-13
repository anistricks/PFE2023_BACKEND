from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Livraison, LigneLivraison
from .serializers import LivraisonSerializer, LigneLivraisonSerializer
from rest_framework.generics import ListAPIView
from rest_framework.exceptions import ValidationError


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
        lignes_data = request.data

        if not isinstance(lignes_data, list):
            raise ValidationError("Les données doivent être une liste d'articles.")

        updated_records = []
        seen_articles = set()  # Utilisez un ensemble pour suivre les articles déjà traités

        for ligne_data in lignes_data:
            article_id = ligne_data.get('article')
            quantite = ligne_data.get('quantite')

            if not article_id:
                raise ValidationError("L'article doit être spécifié avec un ID.")

            # Vérifiez si l'article a déjà été traité
            if article_id in seen_articles:
                ligne_data['isModified'] = True  # Marquez l'article comme étant modifié
            else:
                seen_articles.add(article_id)  # Ajoutez l'article à l'ensemble des articles traités
                ligne_data['isModified'] = False

            # Créez ou mettez à jour l'enregistrement
                existing_record = LigneLivraison.objects.filter(livraison_id=livraison_id, article_id=article_id).first()
            if existing_record:
                serializer = LigneLivraisonSerializer(existing_record, data=ligne_data)
            else:
                serializer = LigneLivraisonSerializer(data=ligne_data)

            if serializer.is_valid():
                updated_record = serializer.save(livraison_id=livraison_id)
                updated_records.append(updated_record)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        return Response([LigneLivraisonSerializer(record).data for record in updated_records], status=status.HTTP_200_OK)
    
    



class GetLivraisonByClientId(ListAPIView):
    serializer_class = LivraisonSerializer

    def get_queryset(self):
        client_id = self.kwargs['client_id']
        return Livraison.objects.filter(client__id=client_id)
