from django.conf.urls import patterns, url


urlpatterns = patterns('',
                       url(r'^$', 'BlogExample.views.home', name='home'),
                       url(r'^login/$', 'django.contrib.auth.views.login', {'template_name': 'BlogExample/login.html'}),
                       url(r'^logout/$', 'BlogExample.views.logout_user'),
                       url(r'^edit/$', 'BlogExample.views.edit', name='edit'),
                       url(r'^edit/(?P<blog_id>[0-9]+)$', 'BlogExample.views.edit', name='edit'),
                       url(r'^delete/(?P<blog_id>[0-9]+)$', 'BlogExample.views.delete', name='delete'),
                       url(r'^blog/(?P<blog_id>[0-9]+)$', 'BlogExample.views.show_blog', name='show_blog')
                       )
