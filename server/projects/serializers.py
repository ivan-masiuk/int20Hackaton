from .models import Project, SearchItem, JoinRequest
from users.serializers import UserShowSerializer, RoleSerializer
from users.models import User
from rest_framework import serializers


class JoinRequestSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(),
        required=False,
    )
    project = serializers.PrimaryKeyRelatedField(
        queryset=Project.objects.all(),
        required=False,
    )
    class Meta:
        model = JoinRequest
        fields = ['id', 'user', 'project', 'status']


class SearchItemSerializer(serializers.ModelSerializer):
    role = RoleSerializer()
    class Meta:
        model = SearchItem
        fields = ['role']


class ProjectSerializer(serializers.ModelSerializer):
    owner = UserShowSerializer()
    users = UserShowSerializer(many=True)
    search_for = SearchItemSerializer(many=True)

    class Meta:
        model = Project
        fields = ('id', 'title', 'overview', 'owner', 'users', 'images', 'created', 'search_for')


class ProjectCreateSerializer(serializers.ModelSerializer):
    search_for = SearchItemSerializer(many=True)
    class Meta:
        model = Project
        fields = ('title', 'overview', 'search_for',)
    def create(self, validated_data):
        search_for_data = validated_data.pop('search_for', [])
        project = Project.objects.create(**validated_data)
        for search_item_data in search_for_data:
            SearchItem.objects.create(project=project, **search_item_data)
        return project

