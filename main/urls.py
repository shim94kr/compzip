from django.conf.urls import patterns, include, url


urlpatterns = patterns('',
    url(r'^$', 'main.views.home', name='home'),
    url(r'^/login$', 'main.views.login', name='login'),
)
