from django.contrib import admin

from models import *

class CommentInline(admin.TabularInline):
    model = Comment
    extra = 1

class TicketAdmin(admin.ModelAdmin):
    inlines = [CommentInline]

class StatusAdmin(admin.ModelAdmin):
    pass

admin.site.register(Ticket, TicketAdmin)
admin.site.register(Status, StatusAdmin)
