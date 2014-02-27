from django.conf.urls import patterns, url
from django.views.generic.base import RedirectView

from home import views
from setsuhi import settings

s3 = settings.S3_STATIC_URL

urlpatterns = patterns('',

    # Place the favicon in a standard static location but still conform to an old fashion favicon
    url(r'^favicon\.ico$', RedirectView.as_view(url=s3+'main/icons/favicon.ico'), name='favicon'),
                       
    url(r'^$', views.front, name='front'),
    url(r'^about/', views.about, name='about'),
    url(r'^media/', views.media, name='media'),
    url(r'^lessons/', views.lessons, name='lessons'),
    url(r'^contact/', views.contact, name='contact'),

)
