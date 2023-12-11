from django.urls import path
from .views import LivraisonList, LivraisonDetail, LigneLivraisonList, LigneLivraisonDetail, ArticlesByLivraisonList

urlpatterns = [
    path('', LivraisonList.as_view(), name='livraison-list'),
    path('<int:livraison_id>/', LivraisonDetail.as_view(), name='livraison-detail'),
    path('lignes_livraison/', LigneLivraisonList.as_view(), name='ligne-livraison-list'),
    path('lignes_livraison/<int:ligne_livraison_id>/', LigneLivraisonDetail.as_view(), name='ligne-livraison-detail'),
    path('<int:livraison_id>/articles/', ArticlesByLivraisonList.as_view(), name='articles-by-livraison-list'),
]
