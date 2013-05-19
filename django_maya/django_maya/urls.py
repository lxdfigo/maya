from django.conf.urls import patterns, include, url
from django_maya.settings import *

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'django_maya.views.home', name='home'),
	url(r'^place/$', 'django_maya.views.place'),
	url(r'^content/(?P<path>.*)','django.views.static.serve',{'document_root':'content'}),
	url(r'^static/(.*)$', 'django.views.static.serve', {'document_root':'static'}),
	url(r'^post/$',  'django_maya.views.postMessage'),
    # url(r'^django_maya/', include('django_maya.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
