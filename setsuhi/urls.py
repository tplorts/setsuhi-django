from django.conf.urls import patterns, include, url

import home
from home import urls

#from django.contrib import admin
#admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'setsuhi.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

#    url(r'^admin/', include(admin.site.urls)),

                       url( r'^', include(home.urls) )
)
