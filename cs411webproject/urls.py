from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'cs411webproject.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'cs411app.views.home'),
    url(r'^login/$', 'cs411app.views.user_login', name='login'),
    url(r'^register/$', 'cs411app.views.register', name='register'),

)
