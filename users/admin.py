from django.contrib import admin

from models import *

class ProjectUserAdmin(admin.ModelAdmin):
    pass

admin.site.register(ProjectUser, ProjectUserAdmin)
