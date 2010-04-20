from django.http import HttpResponse
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
    active_release = Release.objects.get(version=release)
    releases = Release.objects.order_by('release_date').reverse()
    sub_header = str(active_release)
    return render_to_response('downloads/index.html', locals(), context_instance=RequestContext(request))

def download(request, file_id):
    release_file = Release.objects.get(pk=file_id)
    response = HttpResponse(content=release_file.file.chunks(), mimetype="application/octet-stream")
    response['Content-Disposition'] = "attachment; filename=%s" % (release_file.download_name())
    return response
