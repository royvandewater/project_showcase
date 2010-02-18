from django.conf.urls.defaults import *
from django.views.generic.list_detail import object_detail

urlpatterns = patterns('downloads.views',
    (r'download/(?P<file_id>\d+)/$', 'download'),
    (r'(?P<release>[0-9a-zA-Z\.-]+)/$', 'show'),
    (r'^$', 'index'),
)
