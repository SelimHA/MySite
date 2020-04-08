from django.contrib import admin
from .models import Project, projectImage
# Register your models here.
admin.site.register(projectImage)
admin.site.register(Project)