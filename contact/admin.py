from django.contrib import admin
from .models import Contact

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name','email','number',)
    list_display_links = list_display
    list_filter = ('name',)
    search_fields = ('name','email','number')
    # to disbale add functionality
    def has_add_permission(self, request):
        return False
    # to disable change functionality
    def has_change_permission(self, request,obj=None):
        return False

