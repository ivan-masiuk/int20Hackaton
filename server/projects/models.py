from django.utils import timezone
from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Project(models.Model):
    title = models.CharField(max_length=500)
    overview = models.TextField()
    users = models.ManyToManyField(User, related_name='projects')
    images = models.ImageField(upload_to="projects/images/")
    created = models.DateTimeField(default=timezone.now)
