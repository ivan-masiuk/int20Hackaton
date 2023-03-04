from .models import Project
from users.serializers import UserShowSerializer
from rest_framework import serializers


class ProjectSerializer(serializers.ModelSerializer):
    owner = UserShowSerializer()
    users = UserShowSerializer(many=True)

    class Meta:
        model = Project
        fields = ('id', 'title', 'overview', 'owner', 'users', 'images', 'created')
