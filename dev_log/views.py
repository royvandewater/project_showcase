from django.shortcuts import render_to_response
from django.template import RequestContext

import datetime
import simplejson as json

from models import *
from main.models import Content


def index(request):
    content = Content.objects.get(name='dev_log')    
    log = Commit.objects.all().order_by('datetime')
    return render_to_response('dev_log/index.html', locals(), context_instance=RequestContext(request))

def github(request):
    if request.method == "POST":
        if request.POST.has_key('payload'):
            data = json.loads(request.POST['payload'])
            for key in data['commits']:
                commit = Commit()
                commit.commit = key['id']
                commit.commit_url = key['url']
                commit.author = key["author"]["name"]
                commit.message = key["message"]
                commit.datetime = datetime.datetime.strptime(key["timestamp"][:-6], "%Y-%m-%dT%H:%M:%S")
                commit.save()
            message = "Success"
        else:
            message = "Error: Payload not in post data"
    else:
        message = "Error: Method must be post"
    return render_to_response('dev_log/github.html', locals(), context_instance=RequestContext(request))
