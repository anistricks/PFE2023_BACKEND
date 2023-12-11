from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Livraison
from .serializers import LivraisonSerializer

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
