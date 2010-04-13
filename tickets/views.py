from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response
from django.template import RequestContext

from models import *
from main.models import Content

def index(request):
    content = Content.objects.get(name='tickets')
    tickets = Ticket.objects.all()
    return render_to_response('tickets/index.html', locals(), context_instance=RequestContext(request))

@login_required
def new(request):
    return render_to_response('tickets/new.html', locals(), context_instance=RequestContext(request))
