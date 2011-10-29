from django.conf.urls.defaults import patterns, include, url
import views

urlpatterns = patterns('senser.views',
    url(r'^$', views.index),
    url(r'^sense/(\w+)', views.sense),
)