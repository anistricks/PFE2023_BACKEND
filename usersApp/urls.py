from django.urls import path


from .views import UserList,UserDetail,UserModify,UserDelete,UserCreate
    

urlpatterns = [
    path('', UserList.as_view(), name='user-list'),
    path('<str:username>/', UserDetail.as_view(), name='user-detail'),
    path('<str:username>/modify/', UserModify.as_view(), name='user-modify'),
    path('<str:username>/delete/', UserDelete.as_view(), name='user-delete'),
    path('create', UserCreate.as_view(), name='user-create'),
    ] 