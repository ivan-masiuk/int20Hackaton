from django.urls import path
from .views import (
    UserLoginView,
    UserCreateAPIView,
    UserListView,
    UserDetailView,
    RoleListView
)


urlpatterns = [
    path('login/', UserLoginView.as_view(), name='login'),
    path('create/', UserCreateAPIView.as_view(), name='create'),
    path('', UserListView.as_view(), name='list_users'),
    path('<int:pk>/', UserDetailView.as_view(), name='detail_users'),
    path('roles/', RoleListView.as_view(), name='roles_list')
]

