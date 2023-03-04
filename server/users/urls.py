from django.urls import path
from .views import UserLoginView, UserCreateAPIView

urlpatterns = [
    path('login/', UserLoginView.as_view(), name='login'),
    path('create/', UserCreateAPIView.as_view(), name='create'),
]

