from django.urls import path
from .views import ArticleList, ArticleDetail

urlpatterns = [
    path('', ArticleList.as_view(), name='article-list'),
    path('<int:article_id>/', ArticleDetail.as_view(), name='article-detail'),
]