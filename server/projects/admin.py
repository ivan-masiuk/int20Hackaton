from django.contrib import admin
from .models import Project, SearchItem


class SearchItemInline(admin.TabularInline):
    model = SearchItem


class ProjectAdmin(admin.ModelAdmin):
    filter_horizontal = ('users', )
    inlines = [SearchItemInline]


admin.site.register(Project, ProjectAdmin)
admin.site.register(SearchItem)