from django.utils import timezone
from django.contrib.auth import get_user_model
from django.db import models

from users.models import Role


User = get_user_model()


class Project(models.Model):
    title = models.CharField(max_length=500)
    overview = models.TextField()
    owner = models.ForeignKey(User, related_name='owned_projects', on_delete=models.CASCADE)
    users = models.ManyToManyField(User, related_name='projects')
    images = models.ImageField(upload_to="projects/images/")
    created = models.DateTimeField(default=timezone.now)


class SearchItem(models.Model):
    role = models.ForeignKey(Role, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, related_name='search_for', on_delete=models.CASCADE)
    amount = models.IntegerField()


