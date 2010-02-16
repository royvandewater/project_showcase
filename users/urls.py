from django.conf.urls.defaults import *
from django.views.generic.list_detail import object_detail

urlpatterns = patterns('users.views',
    # Library files
    (r'new/$', 'new'),
    (r'login/$', 'login'),
    (r'logout/$', 'destroy'),
    (r'reset/$', 'reset'),
)
