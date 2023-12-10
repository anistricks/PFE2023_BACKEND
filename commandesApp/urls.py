# commandsApp/urls.py
from django.urls import path
from .views import CommandeList, CommandeDetail, LigneCommandeList, LigneCommandeDetail

urlpatterns = [
    path('', CommandeList.as_view(), name='commande-list'),
    path('<int:commande_id>/', CommandeDetail.as_view(), name='commande-detail'),
    path('lignes_commande/', LigneCommandeList.as_view(), name='ligne-commande-list'),
    path('lignes_commande/<int:ligne_commande_id>/', LigneCommandeDetail.as_view(), name='ligne-commande-detail'),
]
