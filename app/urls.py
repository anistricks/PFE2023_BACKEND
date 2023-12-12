"""
URL configuration for app project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from usersApp import urls as userUrls
from articlesApp import urls as articleUrls
from clientsApp import urls as clientUrls
from commandesApp import urls as commandeUrls
from itinerairesApp import urls as itineraireUrls
from livraisonsApp import urls as livraisonUrls
# test pipeline commit test
urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/',include(userUrls)),
    path('articles/', include(articleUrls)),
    path('clients/', include(clientUrls)),
    path('commandes/',include(commandeUrls)),
    path('itineraires/',include(itineraireUrls)),
    path('livraisons/',include(livraisonUrls))
   
]