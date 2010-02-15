from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse

from forms import *
from main.models import Content

def new(request):
    content = Content.objects.get(name='register')
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = User()
            user.username = form.cleaned_data["username"]
            user.first_name = form.cleaned_data["first_name"]
            user.last_name = form.cleaned_data["last_name"]
            user.email = form.cleaned_data["email"]
            user.set_password(form.cleaned_data["password"])
            user.save()
            content.body = ""
            success_message = 'Thank you for registering. Please <a href="{0}">login</a> to get started'.format(reverse('users.views.login'))
    else:
        form = RegisterForm()
    return render_to_response('users/index.html', locals(), context_instance=RequestContext(request))

def login(request):
    pass
