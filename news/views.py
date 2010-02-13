import datetime

from django.shortcuts import render_to_response
from django.template import RequestContext

from models import *
from main.models import Content

def get_article_dates():
    # Get list of all years with articles in them
    years = Article.objects.dates('publish_date', 'year')
    # For each year, get a list of year/month pairs
    dates = dict()
    for year in years:
      dates[year.year] = Article.objects.filter(publish_date__year=year.year).dates('publish_date', 'month')
    # This solution should be worst case O(12n) where n is
    # The number of years
    return dates

def index(request):
    content = Content.objects.get(name='news') 
    articles = Article.objects.order_by('publish_date')[:10]
    dates = get_article_dates()
    return render_to_response('news/index.html', locals(), context_instance=RequestContext(request))

def show(request, year, month):
    content = Content.objects.get(name='archive')
    articles = Article.objects.filter(publish_date__year=year).filter(publish_date__month=month).order_by('publish_date')
    dates = get_article_dates()
    sub_header = datetime.date(int(year), int(month), 1).strftime("%B, %Y")
    return render_to_response('news/index.html', locals(), context_instance=RequestContext(request))
