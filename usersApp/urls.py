from django.urls import path
from .views import UserList, UserDetail
from .views import UserList, UserDetail, TokenObtainPairView, TokenRefreshView,TokenVerifyView
urlpatterns = [
    path('', UserList.as_view(), name='user-list'),
    path('<int:pk>/', UserDetail.as_view(), name='user-detail'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),
]
