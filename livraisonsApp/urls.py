from django.urls import path
from .views import LivraisonList, LivraisonDetail

urlpatterns = [
    path('', LivraisonList.as_view(), name='livraison-list'),
    path('<int:livraison_id>/', LivraisonDetail.as_view(), name='livraison-detail'),
   
]