from django.contrib import admin
from .models import Contact

@admin.register(Contact)
class AuthorAdmin(admin.ModelAdmin):
    # to disbale add functionality
    def has_add_permission(self, request):
        return False
    # to disable change functionality
    def has_change_permission(self, request,obj=None):
        return False

