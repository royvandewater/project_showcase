from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    # (r'^project_showcase/', include('project_showcase.foo.urls')),
    (r'^$', 'news.views.index'),
    (r'^about/', include('about.urls')),
    (r'^downloads/', include('downloads.urls')),
    (r'^log/', include('dev_log.urls')),
    (r'^news/', include('news.urls')),
    (r'^screenshots/', include('screenshots.urls')),
    (r'^users/', include('users.urls')),
    (r'^tickets/', include('tickets.urls')),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^admin/', include(admin.site.urls)),
)
