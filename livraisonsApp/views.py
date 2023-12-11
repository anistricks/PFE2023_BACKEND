from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Livraison, LigneLivraison
from .serializers import LivraisonSerializer, LigneLivraisonSerializer
from rest_framework.generics import ListAPIView

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
