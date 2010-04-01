# Create your views here.
from django.shortcuts import render_to_response
from django.template import RequestContext

from models import *
from main.models import Content

def index(request):
    """
    Loads all screenshots from the latest version
    """
    version = Version.objects.order_by('release_date').reverse()[0]
    return show(request, version.version)

def show(request, version):
    content = Content.objects.get(name="screenshots")
    versions = Version.objects.order_by('release_date').reverse()
    sub_header = Version.objects.get(version=version)
    screenshots = Screenshot.objects.filter(version=sub_header)
    include_fancybox = True
    return render_to_response('screenshots/index.html', locals(), context_instance=RequestContext(request))
