from django.urls import path
from .views import (
    ProjectListView,
    ProjectDetailView,
    CreateProjectAPIView,
    JoinRequestAPIView,
    RejectJoinRequestAPIView,
    AcceptJoinRequestAPIView,
)


urlpatterns = [
    path('', ProjectListView.as_view(), name='projects'),
    path('<int:pk>/', ProjectDetailView.as_view(), name='detail_project'),
    path('create/', CreateProjectAPIView.as_view(), name='create_project'),
    path('<int:project_id>/join-requests/', JoinRequestAPIView.as_view(), name='join-request-list'),
    path('<int:project_id>/join/', JoinRequestAPIView.as_view(), name='join-request-send'),
    path('<int:join_request_id>/accept/', AcceptJoinRequestAPIView.as_view(), name='join-request-accept'),
    path('<int:join_request_id>/reject/', RejectJoinRequestAPIView.as_view(), name='join-request-reject')
]