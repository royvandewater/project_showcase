from django.conf.urls.defaults import *
from django.views.generic.list_detail import object_detail

urlpatterns = patterns('about.views',
    (r'^$', 'index'),
)
