from django.views.generic.simple import direct_to_template
from django.conf.urls.defaults import patterns, include, url
from django.contrib import admin
admin.autodiscover()


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
    url(r'^pagelever', direct_to_template, {'template': 'pagelever.html'}),
    url(r'^kiva', direct_to_template, {'template': 'kiva.html'}),
    url(r'^blurb', direct_to_template, {'template': 'blurb.html'}),
    url(r'^recurly', direct_to_template, {'template': 'recurly.html'}),
    url(r'^songkick', direct_to_template, {'template': 'songkick.html'}),
)

urlpatterns += patterns('django.contrib.staticfiles.views',
    url(r'^static/(?P<path>.*)$', 'serve', kwargs={"insecure": True}),
)
