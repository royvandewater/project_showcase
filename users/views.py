from django.shortcuts import render_to_response
from django.template import RequestContext
# from django.shortcuts import render_to_response
# from django.template import RequestContext

from main.models import Content

def new(request):
    content = Content.objects.get(name='register')
    return render_to_response('users/new.html', locals(), context_instance=RequestContext(request))
