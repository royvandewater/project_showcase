from django.shortcuts import render_to_response
from django.template import RequestContext

from models import *
from main.models import Content

def main(request):
    content = Content.objects.get(name='downloads')
    releases = Release.objects.order_by('release_date').reverse()
    current_release = releases[0]
    sub_header = str(current_release)
    return render_to_response('downloads/downloads.html', locals(), context_instance=RequestContext(request))

def past_release(request, release):
    pass
