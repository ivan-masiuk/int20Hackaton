from django.urls import path
from .views import (
    UserLoginView,
    UserCreateAPIView,
    UserListView,
    UserDetailView,
)


urlpatterns = [
    path('login/', UserLoginView.as_view(), name='login'),
    path('create/', UserCreateAPIView.as_view(), name='create'),
    path('', UserListView.as_view(), name='list_users'),
    path('<int:pk>/', UserDetailView.as_view(), name='detail_users'),
]

