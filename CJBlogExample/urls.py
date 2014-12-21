from django.conf.urls import patterns, url


urlpatterns = patterns('',
                       url(r'^$', 'blog.views.home', name='home'),
                       url(r'^login/$', 'django.contrib.auth.views.login', {'template_name': 'blog/login.html'}),
                       url(r'^logout/$', 'blog.views.logout_user'),
                       url(r'^edit/$', 'blog.views.edit', name='edit'),
                       url(r'^edit/(?P<blog_id>[0-9]+)$', 'blog.views.edit', name='edit'),
                       url(r'^delete/(?P<blog_id>[0-9]+)$', 'blog.views.delete', name='delete'),
                       url(r'^blog/(?P<blog_id>[0-9]+)$', 'blog.views.show_blog', name='show_blog')
                       )
