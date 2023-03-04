from django.urls import path
from .views import (
    ProjectListView,
    ProjectDetailView,
    CreateProjectAPIView,
)


urlpatterns = [
    path('', ProjectListView.as_view(), name='projects'),
    path('<int:pk>/', ProjectDetailView.as_view(), name='detail_project'),
    path('create/', CreateProjectAPIView.as_view(), name='create_project')
]