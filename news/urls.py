from django.conf.urls.defaults import *
from django.views.generic.list_detail import object_detail

urlpatterns = patterns('news.views',
    (r'(\d+)/(\d+)/$', 'archive'),
    (r'^$', 'news'),
)
