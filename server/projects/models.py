from enum import Enum

from django.utils import timezone
from django.contrib.auth import get_user_model
from django.db import models

from users.models import Role


User = get_user_model()


class JoinRequestStatus(Enum):
    PENDING = 'Pending'
    ACCEPTED = 'Accepted'
    REJECTED = 'Rejected'


class Project(models.Model):
    title = models.CharField(max_length=500)
    overview = models.TextField()
    owner = models.ForeignKey(
        User, related_name='owned_projects', on_delete=models.CASCADE
    )
    users = models.ManyToManyField(User, related_name='projects', null=True, blank=True)
    images = models.ImageField(upload_to="projects/images/", default="projects/images/boris.jpeg")
    created = models.DateTimeField(default=timezone.now)


class SearchItem(models.Model):
    role = models.ForeignKey(Role, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, related_name='search_for', on_delete=models.CASCADE)



class JoinRequest(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    status = models.CharField(
        max_length=20,
        choices=[(status.value, status.name) for status in JoinRequestStatus],
        default=JoinRequestStatus.PENDING.value
    )



