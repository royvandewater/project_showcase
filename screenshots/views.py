# Create your views here.
from django.shortcuts import render_to_response
from django.template import RequestContext

from models import *
from main.models import Content

from helpers import *

def main(request):
    """
    Loads all screenshots from the latest version
    """
    content = Content.objects.get(name="screenshots")
    sub_header = get_latest_version()
    screenshots = Screenshot.objects.filter(version=sub_header)
    return render_to_response('screenshots/screenshots.html', locals(), context_instance=RequestContext(request))
