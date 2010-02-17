from django.conf.urls.defaults import *
from django.views.generic.list_detail import object_detail

urlpatterns = patterns('users.views',
    # Library files
    (r'new/$', 'new'),
    (r'login/$', 'login'),
    (r'logout/$', 'destroy'),
    (r'reset/email/(?P<email>[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4})/key/(?P<reset_string>\w+)/$', 'reset'),
    (r'reset/$', 'reset'),
)
