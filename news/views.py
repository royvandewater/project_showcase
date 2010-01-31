from django.shortcuts import render_to_response
from django.template import RequestContext

from models import *
from main.models import Content

def news(request):
    content = Content.objects.get(name='news') 
    articles = Article.objects.order_by('publish_date')[:10]
    artists = SongFile.objects.all().values_list('artist', flat=True)
    return render_to_response('news/news.html', locals(), context_instance=RequestContext(request))
