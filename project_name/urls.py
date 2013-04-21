from django.conf.urls import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'goscalecms_bootstrap.views.home', name='home'),
    # url(r'^goscalecms_bootstrap/', include('goscalecms_bootstrap.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^goscale/', include('goscale.urls')),
    url(r'^accounts/', include('allauth.urls')),
    url(r'^', include('cms.urls')),
) + staticfiles_urlpatterns()
