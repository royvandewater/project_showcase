from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.contrib.auth.models import User
from django.contrib import auth
from django.core.urlresolvers import reverse

from forms import *
from main.models import Content

def new(request):
    content = Content.objects.get(name='register')
    submit_value = "Register"
    submit_action = reverse('users.views.new')
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
    content = Content.objects.get(name='login')
    submit_value = "Login"
    submit_action = reverse('users.views.login')
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = auth.authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password'])
            if user is not None:
                if user.is_active:
                    auth.login(request, user)
                    success_message = "You are now logged in"
                else:
                    error_message = "Account has been disabled"
            else:
                error_message = "Username/password combination not found"
    else:
        form = LoginForm()
    return render_to_response('users/index.html', locals(), context_instance=RequestContext(request))

def destroy(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('news.views.index'))

def reset(request):
    content = Content()
    content.title = "Forgot Password"
    content.header = "Forgot Password"
    content.body = "Enter your email address and you will receive an email with a link to reset your password"
    submit_value = "Submit"
    submit_action = reverse('users.views.reset')

    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = User.objects.get(email=form.cleaned_data['email'])
            content.title = "Forgot Password"
            content.header = "Forgot Password"
            content.body = "An email with the reset link has been sent"
    else:
        form = ResetForm()
    return render_to_response('users/index.html', locals(), context_instance=RequestContext(request))
