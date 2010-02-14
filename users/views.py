from django.shortcuts import render_to_response
from django.template import RequestContext

from forms import *
from main.models import Content

def new(request):
    content = Content.objects.get(name='register')
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            pass
        else:
            pass
    else:
        form = RegisterForm()
    return render_to_response('users/index.html', locals(), context_instance=RequestContext(request))
