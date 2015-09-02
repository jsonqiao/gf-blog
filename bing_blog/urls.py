from django.conf.urls import patterns, url
from bing_blog.views import home_page, hello

urlpatterns = patterns('',
    url(r'^$', home_page),
    url(r'^hello/$', hello),

)
