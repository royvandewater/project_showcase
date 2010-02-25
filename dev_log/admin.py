from django.contrib import admin

from models import *

class CommitAdmin(admin.ModelAdmin):
    list_display = ('datetime','author','message','commit')
    search_fields = ['author','message']

admin.site.register(Commit, CommitAdmin)
