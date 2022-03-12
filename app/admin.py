from django.contrib import admin
from .models import User, Project

class ProjectAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}

# Register your models here.
admin.site.register(User)
admin.site.register(Project, ProjectAdmin)