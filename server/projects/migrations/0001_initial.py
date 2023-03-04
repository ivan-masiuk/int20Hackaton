# Generated by Django 4.1.7 on 2023-03-04 18:40

from django.conf import settings
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Project",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=500)),
                ("overview", models.TextField()),
                ("images", models.ImageField(upload_to="projects/images/")),
                ("created", models.DateTimeField(default=django.utils.timezone.now)),
                (
                    "users",
                    models.ManyToManyField(
                        related_name="projects", to=settings.AUTH_USER_MODEL
                    ),
                ),
            ],
        ),
    ]