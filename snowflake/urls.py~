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
    url(r'^blog/', include('blog.urls')),
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
    url(r'^exec', direct_to_template, {'template':'exec.html'}),
    url(r'^roblox', direct_to_template, {'template':'roblox.html'}),
    url(r'^resume', direct_to_template, {'template':'resume.html'}),
    url(r'^json_test', 'snowflake.frontend.views.json_test'),                       
    url(r'^alert', 'snowflake.frontend.views.alert'),
)

urlpatterns += patterns('django.contrib.staticfiles.views',
    url(r'^static/(?P<path>.*)$', 'serve', kwargs={"insecure": True}),
)
