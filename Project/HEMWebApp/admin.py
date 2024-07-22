from django.contrib import admin
from .models import Project


# Register your models here.

class ProjectAdmin(admin.ModelAdmin):
    list_display = ['name', 'numroom','created_by', 'date_created']
    list_filter = ['created_by']
    search_fields = ['name', 'created_by']
    date_hierarchy = 'date_created'


admin.site.register(Project, ProjectAdmin)
