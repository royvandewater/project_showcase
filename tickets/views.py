# Create your views here.

def index(request):
    tickets = Ticket.objects.all()
    return render_to_response('tickets/index.html', locals(), context_instance=RequestContext(request))
