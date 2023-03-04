from .models import Project, SearchItem
from users.serializers import UserShowSerializer
from rest_framework import serializers


class ProjectSerializer(serializers.ModelSerializer):
    owner = UserShowSerializer()
    users = UserShowSerializer(many=True)

    class Meta:
        model = Project
        fields = ('id', 'title', 'overview', 'owner', 'users', 'images', 'created')


class SearchItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = SearchItem
        fields = ['role']


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

