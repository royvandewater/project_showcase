from django.contrib import admin
from models import *

class ScreenshotAdmin(admin.ModelAdmin):
    pass

class VersionAdmin(admin.ModelAdmin):
    pass

admin.site.register(Screenshot, ScreenshotAdmin)
admin.site.register(Version, VersionAdmin)
