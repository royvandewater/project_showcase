from django.shortcuts import render_to_response
from django.template import RequestContext

from models import *

def index(request):
    tickets = Ticket.objects.all()
    return render_to_response('tickets/index.html', locals(), context_instance=RequestContext(request))
