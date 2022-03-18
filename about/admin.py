from django.contrib import admin
from .models import AboutMain,AboutSubject

@admin.register(AboutSubject)
class AboutSubjectAdmin(admin.ModelAdmin):
    list_display = ('Subject','date',)
    list_display_links = list_display
    list_filter = ('Subject','date',)
    search_fields = ('Subject',)


@admin.register(AboutMain)
class AuthorAdmin(admin.ModelAdmin):
    # to disbale add functionality
    def has_add_permission(self, request):
        return False

    # to disable delete functionaliyt
    def has_delete_permission(self, request, obj=None):
        return False