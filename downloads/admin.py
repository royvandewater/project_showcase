from django.contrib import admin
from models import *

class ReleaseAdmin(admin.ModelAdmin):
    pass

admin.site.register(Release, ReleaseAdmin)
