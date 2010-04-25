from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.shortcuts import render_to_response
from django.template import RequestContext
from forms import *
from main.models import Content
from models import *


def index(request):
    content = Content.objects.get(name='tickets')
    tickets = Ticket.objects.all()
    return render_to_response('tickets/index.html', locals(), context_instance=RequestContext(request))

@login_required
def new(request):
    if request.method == 'POST':
        form = NewTicketForm(request.POST)
        if form.is_valid():
            ticket = Ticket()
            ticket.name     = form.cleaned_data['name']
            ticket.priority = form.cleaned_data['priority']
            ticket.description = form.cleaned_data["description"]
            ticket.status = Status.objects.get(name="new")
            ticket.creator = ProjectUser.objects.get(user=request.user.pk)
            ticket.save()
            success_message = "Ticket submitted"
    else:
        form = NewTicketForm()

    submit_value = "Create"
    submit_action = reverse('tickets.views.new')
    return render_to_response('tickets/new.html', locals(), context_instance=RequestContext(request))

def show(request, ticket):
    return render_to_response('tickets/new.html', locals(), context_instance=RequestContext(request))
