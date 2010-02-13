from django.shortcuts import render_to_response
from django.template import RequestContext

from models import *
from main.models import Content

# Create your views here.
def index(request):
    content = Content.objects.get(name='about')
    return render_to_response('about/index.html', locals(), context_instance=RequestContext(request))
