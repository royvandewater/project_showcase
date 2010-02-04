# Create your views here.
from django.shortcuts import render_to_response
from django.template import RequestContext

from models import *

def main(request):
    return render_to_response('screenshots/screenshots.html', locals(), context_instance=RequestContext(request))
