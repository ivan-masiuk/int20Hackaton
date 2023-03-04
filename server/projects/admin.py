from django.contrib import admin
from .models import Project


class ProjectAdmin(admin.ModelAdmin):
    filter_horizontal = ('users', )


admin.site.register(Project, ProjectAdmin)

