from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.sites.models import Site
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from django.core.mail import send_mail


# Disable import sha warning
import warnings
warnings.simplefilter("ignore",DeprecationWarning)

import sha
import random

from forms import *
from main.models import Content
from models import *

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

            project_user = ProjectUser()
            project_user.user = user
            project_user.save()

            content.body = ""
            success_message = 'Thank you for registering. Please <a href="' + reverse('users.views.login') + '">login</a> to get started'
    else:
        form = RegisterForm()
    return render_to_response('users/index.html', locals(), context_instance=RequestContext(request))

def login(request):
    content = Content.objects.get(name='login')
    content.body += '<br><a href="' + reverse('users.views.forgot') + '" class="forgot_password_link">forgot password?</a>'
    submit_value = "Login"
    submit_action = reverse('users.views.login')
    # Set the callback url
    try:
        callback_url = request.GET["next"]
    except KeyError:
        callback_url = ""

    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = auth.authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password'])
            if user is not None:
                if user.is_active:
                    auth.login(request, user)
                    success_message = "You are now logged in"
                    if callback_url:
                        return HttpResponseRedirect(callback_url)
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

def forgot(request):
    content = Content()
    content.title = "Forgot Password"
    content.header = "Forgot Password"
    content.body = "Enter your email address and you will receive an email with a link to reset your password"
    submit_value = "Submit"
    submit_action = reverse('users.views.forgot')

    if request.method == 'POST':
        form = ResetForm(request.POST)
        if form.is_valid():
            user = User.objects.filter(email=form.cleaned_data['email'])
            if user > 0:
                user = ProjectUser.objects.get(user=user[0])

                user.reset_string = sha.sha(str(random.random())).hexdigest()
                user.save()

                current_site = Site.objects.get_current()
                email_message = """
                    Click this link to reset your password,
                    http://""" + current_site.domain + reverse("users.views.reset", kwargs={'email':user.user.email, 'reset_string':user.reset_string})

            send_mail("Partybeat password reset", email_message, "support@partybeat.net", [user.user.email], fail_silently=False)

            content.body = "An email with the reset link has been sent"
    else:
        form = ResetForm()

    return render_to_response('users/index.html', locals(), context_instance=RequestContext(request))

def reset(request, email, reset_string):
    content = Content()
    content.title = "Password Reset"
    content.header = "Password Reset"
    content.body = ""

    user = User.objects.filter(email=email)
    if user:
        user = ProjectUser.objects.get(user=user[0])

    if user and user.reset_string == reset_string:
        if request.method == 'POST':
            form = ResetPasswordForm(request.POST)
            if form.is_valid():
                user.user.set_password(form.cleaned_data["password"])
                user.reset_string = None
                user.user.save()
                user.save()
                success_message = 'Your password has been updated. Please try to <a href="%s">log in</a>' % (reverse('users.views.login'))
        else:
            content.body = "Please enter a new password"
            form = ResetPasswordForm()
        submit_value = "Submit"
        submit_action = reverse('users.views.reset', kwargs={'email':email, 'reset_string':reset_string})
    else:
        success_message = "The email address or reset key is incorrect. Please use the url provided in the password reset email"
    return render_to_response('users/index.html', locals(), context_instance=RequestContext(request))
