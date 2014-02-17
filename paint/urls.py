from django.conf.urls import patterns, include, url
from paintapp.views import paint, files, search


from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'paint.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', paint),
    url(r'^files/', files),
    url(r'^search/', search),
)
