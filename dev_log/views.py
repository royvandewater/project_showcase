from django.shortcuts import render_to_response
from django.template import RequestContext

from models import *
from main.models import Content

def index(request):
    content = Content.objects.get(name='dev_log')    
    log = LogEntry.objects.all().order_by('datetime')
    return render_to_response('dev_log/index.html', locals(), context_instance=RequestContext(request))
