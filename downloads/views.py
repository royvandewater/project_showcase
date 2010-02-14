from django.shortcuts import render_to_response
from django.template import RequestContext

from models import *
from main.models import Content

def index(request):
    content = Content.objects.get(name='downloads')
    releases = Release.objects.order_by('release_date').reverse()
    active_release = releases[0]
    sub_header = str(active_release)
    return render_to_response('downloads/index.html', locals(), context_instance=RequestContext(request))

def show(request, release):
    content = Content.objects.get(name='downloads')
    active_release = Release.objects.get(version=float(release))
    releases = Release.objects.order_by('release_date').reverse()
    sub_header = str(active_release)
    return render_to_response('downloads/index.html', locals(), context_instance=RequestContext(request))
