from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext

from models import *
from main.models import Content

def load_content(function):
    def wrapper(*args, **kwargs):
        content = Content.objects.get(name='downloads')
        releases = Release.objects.order_by('release_date').reverse()
        return function(content=content, releases=releases, *args, **kwargs)
    return wrapper

@load_content
def index(request, content, releases):
    return show(request, release=releases[0])

@load_content
def show(request, content, releases, release):
    active_release = Release.objects.get(version=release)
    sub_header = str(active_release)
    return render_to_response('downloads/index.html', locals(), context_instance=RequestContext(request))

def download(request, file_id):
    release_file = Release.objects.get(pk=file_id)
    response = HttpResponse(content=release_file.file.chunks(), mimetype="application/octet-stream")
    response['Content-Disposition'] = "attachment; filename=%s" % (release_file.download_name())
    return response
