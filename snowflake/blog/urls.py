from django.views.generic.simple import direct_to_template
from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('',
    url(r'^$', 'blog.views.home'),                       
    url(r'^(?P<blog>\d+)/', 'blog.views.single_post'),                       
    url(r'^tags/(?P<tag>\d+)/', 'blog.views.tag_search'),
    url(r'^enter/', 'blog.views.enter_post'),
)

urlpatterns += patterns('django.contrib.staticfiles.views',
    url(r'^static/(?P<path>.*)$', 'serve', kwargs={"insecure": True}),
)
