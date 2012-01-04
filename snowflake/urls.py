from django.conf.urls.defaults import patterns, include, url
from django.contrib import admin
admin.autodiscover()
import django_cron
django_cron.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'snowflake.frontend.views.home'),
    url(r'^cv/', 'snowflake.frontend.views.cv'),
    url(r'^projects/', 'snowflake.frontend.views.projects'),
    url(r'^links/', 'snowflake.frontend.views.links'),
    url(r'^quotes/', 'snowflake.frontend.views.quotes'),
    url(r'^blog/', 'snowflake.frontend.views.blog'),
    url(r'^contact/', 'snowflake.frontend.views.contact'),    
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'derain/', 'snowflake.frontend.views.derain'),                   
    url(r'send_email', 'snowflake.frontend.views.send_email'),
)

urlpatterns += patterns('django.contrib.staticfiles.views',
    url(r'^static/(?P<path>.*)$', 'serve', kwargs={"insecure": True}),
)
