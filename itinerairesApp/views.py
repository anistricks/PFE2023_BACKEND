from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Itineraire
from .serializers import ItineraireSerializer

class ItineraireList(APIView):
    def get(self, request):
        itineraires = Itineraire.objects.all()
        serializer = ItineraireSerializer(itineraires, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ItineraireSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ItineraireDetail(APIView):
    def get_object(self, itineraire_id):
        return get_object_or_404(Itineraire, id=itineraire_id)

    def get(self, request, itineraire_id):
        itineraire = self.get_object(itineraire_id)
        serializer = ItineraireSerializer(itineraire)
        return Response(serializer.data)

    def put(self, request, itineraire_id):
        itineraire = self.get_object(itineraire_id)
        serializer = ItineraireSerializer(itineraire, data=request.data)
        if serializer.is_valid():
            serializer.save()

           
            commandes_ids = request.data.get('commandes', [])

           
            itineraire.commandes.set(commandes_ids)

            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
