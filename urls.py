from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    # (r'^project_showcase/', include('project_showcase.foo.urls')),
    (r'^$', 'news.views.news'),
    (r'^archive/(\d+)/(\d+)/$', 'news.views.archive'),
    (r'^about/$', 'about.views.about'),
    (r'^screenshots/(?P<version>[0-9a-zA-Z\.-]+)/$', 'screenshots.views.past_version'),
    (r'^screenshots/$', 'screenshots.views.main'),
    (r'^downloads/$', 'downloads.views.main'),
    (r'^downloads/(?P<release>[0-9a-zA-Z\.-]+)/$', 'downloads.views.past_release'),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^admin/', include(admin.site.urls)),
)
