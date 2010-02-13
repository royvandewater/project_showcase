from django.conf.urls.defaults import *
from django.views.generic.list_detail import object_detail

urlpatterns = patterns('screenshots.views',
    (r'(?P<version>[0-9a-zA-Z\.-]+)/$', 'show'),
    (r'^$', 'index'),
)
