from django.contrib import admin
from .models import Project, Room


# Register your models here.

class ProjectAdmin(admin.ModelAdmin):
    list_display = ['name', 'numroom', 'created_by', 'date_created']
    list_filter = ['created_by']
    search_fields = ['name', 'created_by']
    date_hierarchy = 'date_created'


class RoomAdmin(admin.ModelAdmin):
    list_display = ['name', 'app', 'projectname', 'date_created']
    list_filter = ['projectname']
    search_fields = ['name', 'projectname']
    date_hierarchy = 'date_created'


admin.site.register(Project, ProjectAdmin)
admin.site.register(Room, RoomAdmin)
