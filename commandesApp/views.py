# commandsApp/views.py
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Commande, LigneCommande
from .serializers import CommandeSerializer, LigneCommandeSerializer
from rest_framework.generics import ListAPIView
class CommandeList(APIView):
    def get(self, request):
        commandes = Commande.objects.all()
        serializer = CommandeSerializer(commandes, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CommandeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CommandeDetail(APIView):
    def get_object(self, commande_id):
        return get_object_or_404(Commande, id=commande_id)

    def get(self, request, commande_id):
        commande = self.get_object(commande_id)
        serializer = CommandeSerializer(commande)
        return Response(serializer.data)

    def put(self, request, commande_id):
        commande = self.get_object(commande_id)
        serializer = CommandeSerializer(commande, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, commande_id):
        commande = self.get_object(commande_id)
        commande.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class LigneCommandeList(APIView):
    def get(self, request):
        lignes_commande = LigneCommande.objects.all()
        serializer = LigneCommandeSerializer(lignes_commande, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = LigneCommandeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LigneCommandeDetail(APIView):
    def get_object(self, ligne_commande_id):
        return get_object_or_404(LigneCommande, id=ligne_commande_id)

    def get(self, request, ligne_commande_id):
        ligne_commande = self.get_object(ligne_commande_id)
        serializer = LigneCommandeSerializer(ligne_commande)
        return Response(serializer.data)

    def put(self, request, ligne_commande_id):
        ligne_commande = self.get_object(ligne_commande_id)
        serializer = LigneCommandeSerializer(ligne_commande, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, ligne_commande_id):
        ligne_commande = self.get_object(ligne_commande_id)
        ligne_commande.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class ArticlesByCommandeList(ListAPIView):
    serializer_class = LigneCommandeSerializer

    def get_queryset(self):
        commande_id = self.kwargs['commande_id']
        return LigneCommande.objects.filter(commande__id=commande_id)   