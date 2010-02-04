# Create your views here.
from django.shortcuts import render_to_response
from django.template import RequestContext

from models import *
from main.models import Content

from helpers import *

def main(request):
    content = Content.objects.get(name="screenshots")
    return render_to_response('screenshots/screenshots.html', locals(), context_instance=RequestContext(request))
