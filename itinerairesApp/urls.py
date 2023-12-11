from django.urls import path
from .views import ItineraireList, ItineraireDetail

urlpatterns = [
    path('', ItineraireList.as_view(), name='itineraire-list'),
    path('<int:itineraire_id>/', ItineraireDetail.as_view(), name='itineraire-detail'),
   
]