from django.contrib import admin

from models import *

class ContentAdmin(admin.ModelAdmin):
    pass

class SettingAdmin(admin.ModelAdmin):
    list_display = ('name','active')

admin.site.register(Content, ContentAdmin)
admin.site.register(Setting, SettingAdmin)
