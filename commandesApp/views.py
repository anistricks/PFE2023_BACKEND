# commandsApp/views.py
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Commande, LigneCommande
from commandesApp.models import Client
from .serializers import CommandeSerializer, LigneCommandeSerializer
from rest_framework.generics import ListAPIView
from rest_framework.exceptions import ValidationError
class CommandeList(APIView):
    def get(self, request):
        commandes = Commande.objects.all()
        serializer = CommandeSerializer(commandes, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CommandeSerializer(data=request.data)
        if serializer.is_valid():
            client_id = serializer.validated_data['client'].id
            existing_commande = Commande.objects.filter(client=client_id).exists()
            if existing_commande:
                raise ValidationError("Ce client a déjà une commande en cours. Veuillez la modifier.")
            
           
            serializer.save()

           
            nouvelle_commande_id = serializer.instance.id

           
            response_data = {
                "id_commande": nouvelle_commande_id,
                "message": "Commande créée avec succès."
            }

            return Response(response_data, status=status.HTTP_201_CREATED)
        
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
        return LigneCommande.objects.filter(commande_id=commande_id)   
    def post(self, request, commande_id):
        commande = Commande.objects.get(id=commande_id)
        serializer = LigneCommandeSerializer(data=request.data)

        if serializer.is_valid():
           
            article_id = serializer.validated_data['article'].id
            existing_ligne_commande = LigneCommande.objects.filter(commande=commande, article=article_id).exists()
            
            if existing_ligne_commande:
                return Response({"detail": "Cette ligne de commande existe déjà pour cette commande."}, status=status.HTTP_400_BAD_REQUEST)
            
            ligne_commande = serializer.save(commande=commande)
            return Response(LigneCommandeSerializer(ligne_commande).data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def put(self, request, commande_id):
        commande = Commande.objects.get(id=commande_id)
        article_id = request.data.get('article', None)
        quantite = request.data.get('quantite', None)

        if article_id is not None and quantite is not None:
            try:
               
                lignes_commande = LigneCommande.objects.filter(commande=commande, article=article_id)
                
                if lignes_commande.exists():
                    
                    ligne_commande = lignes_commande.first()
                    ligne_commande.quantite = quantite
                    ligne_commande.save()
                    serializer = LigneCommandeSerializer(ligne_commande)
                    return Response(serializer.data, status=status.HTTP_200_OK)
                else:
                    return Response({"detail": "La ligne de commande n'existe pas pour cet article."}, status=status.HTTP_404_NOT_FOUND)
            except LigneCommande.DoesNotExist:
                return Response({"detail": "La ligne de commande n'existe pas pour cet article."}, status=status.HTTP_404_NOT_FOUND)
        else:
            return Response({"detail": "L'article et la quantité sont requis."}, status=status.HTTP_400_BAD_REQUEST)

class CommandeClient(ListAPIView):
    def delete(self, request, client_id):
        commandes = Commande.objects.filter(client__id=client_id)
        
        if commandes.exists():
            commandes.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)
