from django.contrib import admin
from .models import Blog,Comment

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('__str__','title','date')
    list_display_links = list_display
    list_filter = ('creator_name','date',)
    search_fields = ('creator_name',)

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name','date','status')
    list_display_links = list_display
    list_filter = ('name','status','date',)


    # to disbale add functionality
    def has_add_permission(self, request):
        return False
    


