from django.shortcuts import render_to_response
from django.template import RequestContext

from models import *

def news(request):
    return render_to_response('news.html', locals(), context_instance=RequestContext(request))
