from django.contrib import admin

from models import *

class TicketAdmin(admin.ModelAdmin):
    pass

class StatusAdmin(admin.ModelAdmin):
    pass

admin.site.register(Ticket, TicketAdmin)
admin.site.register(Status, StatusAdmin)
