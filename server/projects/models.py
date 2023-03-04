from django.utils import timezone

from django.db import models


class Project(models.Model):
    title = models.CharField(max_length=500)
    overview = models.TextField()
    # user_m2m
    images = models.ImageField(upload_to="projects/images/")
    created = models.DateTimeField(default=timezone.now)
