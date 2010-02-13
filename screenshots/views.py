# Create your views here.
from django.shortcuts import render_to_response
from django.template import RequestContext

from models import *
from main.models import Content

def main(request):
    """
    Loads all screenshots from the latest version
    """
    content = Content.objects.get(name="Screenshots")
    versions = Version.objects.order_by('release_date').reverse()
    sub_header = versions[0]
    screenshots = Screenshot.objects.filter(version=sub_header)
    include_fancybox = True
    return render_to_response('screenshots/screenshots.html', locals(), context_instance=RequestContext(request))

def past_version(request, version):
    content = Content.objects.get(name="screenshots")
    versions = Version.objects.order_by('release_date').reverse()
    sub_header = Version.objects.get(version=version)
    screenshots = Screenshot.objects.filter(version=sub_header)
    include_fancybox = True
    return render_to_response('screenshots/screenshots.html', locals(), context_instance=RequestContext(request))
    pass
