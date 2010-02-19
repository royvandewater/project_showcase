from django.contrib import admin

from models import *

class LogEntryAdmin(admin.ModelAdmin):
    list_display = ('datetime','author','description','commit')
    search_fields = ['author','description']

admin.site.register(LogEntry, LogEntryAdmin)
