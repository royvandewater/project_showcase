from django.shortcuts import render_to_response
from django.template import RequestContext

from main.models import Content

def main(request):
    content = Content.objects.get(name='downloads')
    return render_to_response('downloads/downloads.html', locals(), context_instance=RequestContext(request))
