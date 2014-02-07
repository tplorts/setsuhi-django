from django.conf.urls import patterns, url

from home import views

urlpatterns = patterns('',
    url(r'^$', views.front, name='front'),
    url(r'^about/', views.about, name='about'),
# mada..    url(r'^artwork/', views.artwork, name='artwork'),
    url(r'^media/', views.media, name='media'),
    url(r'^lessons/', views.lessons, name='lessons'),
    url(r'^contact/', views.contact, name='contact'),
# mada..    url(r'^blog/', views.blog, name='blog'),
)
