from django.conf.urls import patterns, url
from bing_blog.views import index, hello

urlpatterns = patterns('',
    url(r'^', index),
    url(r'^hello/$', hello),

)
