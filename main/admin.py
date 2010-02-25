from django.contrib import admin

from models import *

class ContentAdmin(admin.ModelAdmin):
    pass

class SettingAdmin(admin.ModelAdmin):
    list_display = ('name','active','github_url')
    fieldsets = [
            (None,                  {'fields': ['name', 'active']}),
            ('Github integration',  {'fields': ['git_key']}),
    ]

admin.site.register(Content, ContentAdmin)
admin.site.register(Setting, SettingAdmin)
