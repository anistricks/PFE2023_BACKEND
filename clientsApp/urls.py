from django.urls import path
from .views import ClientList, ClientDetail

urlpatterns = [
    path('', ClientList.as_view(), name='client-list'),
    path('<int:client_id>/', ClientDetail.as_view(), name='client-detail'),
]
