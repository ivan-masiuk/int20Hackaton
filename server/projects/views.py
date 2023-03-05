from rest_framework import generics, status
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.pagination import PageNumberPagination
import json

from .models import Project, JoinRequest, JoinRequestStatus
from .serializers import ProjectSerializer, ProjectCreateSerializer, JoinRequestSerializer


class JoinRequestAPIView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request, project_id):
        # Get the project object
        try:
            project = Project.objects.get(id=project_id)
        except Project.DoesNotExist:
            return Response({'detail': 'Project not found'}, status=status.HTTP_404_NOT_FOUND)

        # Check if the user has already sent a join request
        existing_request = JoinRequest.objects.filter(user=request.user, project=project).first()
        if existing_request:
            return Response({'detail': 'You have already sent a join request'}, status=status.HTTP_400_BAD_REQUEST)

        if project.owner == request.user:
            return Response({"error": "Project owner cannot send a request to join"},
                            status=status.HTTP_400_BAD_REQUEST)
        if project.users.filter(pk=request.user.pk).exists():
            return Response({"error": "User is already a member of the project"}, status=status.HTTP_400_BAD_REQUEST)

        # Create the join request
        serializer = JoinRequestSerializer(data=request.data)
        if serializer.is_valid():
            join_request = serializer.save(user=request.user, project=project)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, project_id):
        # Get the project object
        try:
            project = Project.objects.get(id=project_id)
        except Project.DoesNotExist:
            return Response({'detail': 'Project not found'}, status=status.HTTP_404_NOT_FOUND)

        # Check if the user is the owner of the project
        if project.owner != request.user:
            return Response({'detail': 'Only the project owner can view join requests'}, status=status.HTTP_403_FORBIDDEN)

        # Get the join requests for the project
        join_requests = JoinRequest.objects.filter(project=project)
        serializer = JoinRequestSerializer(join_requests, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class AcceptJoinRequestAPIView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request, join_request_id):
        try:
            join_request = JoinRequest.objects.get(id=join_request_id)
        except JoinRequest.DoesNotExist:
            return Response({'detail': 'Join request not found'}, status=status.HTTP_404_NOT_FOUND)

        project = join_request.project
        if project.owner != request.user:
            return Response({'detail': 'Only the project owner can accept join requests'}, status=status.HTTP_403_FORBIDDEN)

        join_request.status = JoinRequestStatus.ACCEPTED.value
        join_request.save()

        project.users.add(join_request.user)
        project.search_for.filter(role=join_request.user.role).first().delete()

        return Response({'detail': 'Join request accepted'}, status=status.HTTP_200_OK)


class RejectJoinRequestAPIView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request, join_request_id):
        try:
            join_request = JoinRequest.objects.get(id=join_request_id)
        except JoinRequest.DoesNotExist:
            return Response({'detail': 'Join request not found'}, status=status.HTTP_404_NOT_FOUND)

        project = join_request.project
        if project.owner != request.user:
            return Response({'detail': 'Only the project owner can reject join requests'}, status=status.HTTP_403_FORBIDDEN)

        join_request.delete()
        # join_request.status = JoinRequestStatus.REJECTED.value
        # join_request.save()

        return Response({'detail': 'Join request rejected'}, status=status.HTTP_200_OK)


class CreateProjectAPIView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):
        data = request.data
        new_data = dict()

        new_data['search_for'] = json.loads(data['search_for'])
        new_data['title'] = data['title']
        new_data['overview'] = data['overview']
        serializer = ProjectCreateSerializer(data=new_data)
        if serializer.is_valid():
            project = serializer.save(owner=request.user)
            project.images = data['file']
            project.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProjectListView(generics.ListAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = ProjectSerializer
    queryset = Project.objects.all()

    def get_queryset(self):
        # Get the role of the current user
        user_role = self.request.user.role

        # Get the projects where the current user's role is searched for
        queryset = Project.objects.filter(search_for__role=user_role)

        return queryset


class ProjectDetailView(generics.RetrieveAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    serializer_class = ProjectSerializer
    queryset = Project.objects.all()
