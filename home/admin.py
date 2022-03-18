from django.contrib import admin
from .models import Projects,SingleProject

@admin.register(SingleProject)
class SingleProjectAdmin(admin.ModelAdmin):
    list_display = ('project_name','role','agency',)
    list_display_links = list_display
    list_filter = ('role','agency','date')
    search_fields = ('project_name','role','agency',)

@admin.register(Projects)
class ProjectsAdmin(admin.ModelAdmin):
    # to disbale add functionality
    def has_add_permission(self, request):
        return False
    # to disable delete functionaliyt
    def has_delete_permission(self, request, obj=None):
        return False