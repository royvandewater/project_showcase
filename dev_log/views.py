from django.shortcuts import render_to_response
from django.template import RequestContext
from django.views.decorators.csrf import csrf_exempt
from django.db import IntegrityError

import datetime
import simplejson as json

from models import *
import helpers
from main.models import Content
from main.models import Setting

def index(request):
    content = Content.objects.get(name='dev_log')    
    log = Commit.objects.all().order_by('datetime').reverse()[:10]
    return render_to_response('dev_log/index.html', locals(), context_instance=RequestContext(request))

@csrf_exempt
def github(request, git_key):
    if request.method == "POST":
        if request.POST.has_key('payload'):
            if git_key == Setting.objects.get(active=True).git_key:
                data = json.loads(request.POST['payload'])
                for key in data['commits']:
                    try:
                        commit = Commit()
                        commit.commit = key['id']
                        commit.commit_url = key['url']
                        commit.author = key["author"]["name"]
                        commit.message = key["message"]
                        commit.datetime = helpers.parse_datetime(key["timestamp"])
                        commit.save()
                    except IntegrityError:
                        pass
                message = "Success"
            else:
                message = "Error: Github key incorrect"
        else:
            message = "Error: Payload not in post data"
    else:
        message = "Error: Method must be post"
    return render_to_response('dev_log/github.html', locals(), context_instance=RequestContext(request))
