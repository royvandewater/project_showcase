from django.conf.urls.defaults import *
from django.views.generic.list_detail import object_detail

urlpatterns = patterns('tickets.views',
    (r'^$', 'index'),
    (r'new/$', 'new'),
    (r'show/(?P<ticket>\d+)/$', 'show'),
)