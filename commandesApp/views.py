from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Commande, LigneCommande
from .serializers import CommandeSerializer, LigneCommandeSerializer
from rest_framework.generics import ListAPIView
from rest_framework.exceptions import ValidationError
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework import status
from .models import Commande
from .serializers import CommandeSerializer
from articlesApp.models import  Article


class CommandeList(APIView):
    def get(self, request):
        commandes = Commande.objects.all()
        serializer = CommandeSerializer(commandes, many=True)
        return Response(serializer.data)

    def post(self, request):
       
        serializer = CommandeSerializer(data=request.data)

        if serializer.is_valid():
            
            client = serializer.validated_data['client']

           
            commande = serializer.save()

           
            articles_disponibles = Article.objects.all()

            
            lignes_commande = []
            for article in articles_disponibles:
                ligne_commande_data = {
                    'article': article,
                    'quantite': 0.0  
                }
                lignes_commande.append(ligne_commande_data)

            
            for ligne_commande_data in lignes_commande:
                ligne_commande_data['commande'] = commande
            lignes_commande_objects = LigneCommande.objects.bulk_create([LigneCommande(**data) for data in lignes_commande])

            
            if len(lignes_commande_objects) == len(lignes_commande):
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                raise ValidationError("Erreur lors de la création des lignes de commande.")
        else:
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
        data = request.data

        if isinstance(data, list):
            serializer = LigneCommandeSerializer(data=data, many=True)

            if serializer.is_valid():
                for item in serializer.validated_data:
                    article_id = item['article'].id
                    existing_ligne_commande = LigneCommande.objects.filter(commande=commande, article=article_id).exists()

                    if existing_ligne_commande:
                        return Response({"detail": "Cette ligne de commande existe déjà pour cette commande."}, status=status.HTTP_400_BAD_REQUEST)

                serializer.save(commande=commande)
                return Response(serializer.data, status=status.HTTP_201_CREATED)

            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({"detail": "La requête doit contenir une liste d'articles avec quantités."}, status=status.HTTP_400_BAD_REQUEST)
    def put(self, request, commande_id):
        commande = Commande.objects.get(id=commande_id)
        articles_data = request.data.get('articles', None)

        if articles_data is not None:
            try:
                for article_info in articles_data:
                    article_id = article_info.get('article', None)
                    quantite = article_info.get('quantite', None)

                    if article_id is not None and quantite is not None:
                        lignes_commande = LigneCommande.objects.filter(commande=commande, article=article_id)

                        if lignes_commande.exists():
                            ligne_commande = lignes_commande.first()
                            ligne_commande.quantite = quantite
                            ligne_commande.save()
                        else:
                           
                            LigneCommande.objects.create(commande=commande, article=article_id, quantite=quantite)
                    else:
                        return Response({"detail": "L'article et la quantité sont requis."}, status=status.HTTP_400_BAD_REQUEST)

                
                updated_articles = LigneCommande.objects.filter(commande=commande)
                serializer = LigneCommandeSerializer(updated_articles, many=True)
                return Response(serializer.data, status=status.HTTP_200_OK)

            except LigneCommande.DoesNotExist:
                return Response({"detail": "La ligne de commande n'existe pas pour cet article."}, status=status.HTTP_404_NOT_FOUND)
        else:
            return Response({"detail": "La liste des articles et quantités est requise."}, status=status.HTTP_400_BAD_REQUEST)

class CommandeClient(ListAPIView):
    serializer_class = LigneCommandeSerializer
    def get_queryset(self):
        client_id = self.kwargs['client_id']
        return LigneCommande.objects.filter(commande__client_id=client_id)
      
    def delete(self, request, client_id):
        commandes = Commande.objects.filter(client__id=client_id)
        
        if commandes.exists():
            commandes.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)

class GetCommandeByClientId(ListAPIView):
    def get_queryset(self):
        client_id = self.kwargs['client_id']
        return Commande.objects.filter(client__id=client_id)

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        commande_ids = queryset.values_list('id', flat=True)
        return Response(commande_ids)