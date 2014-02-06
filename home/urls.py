from django.conf.urls import patterns, url

from home import views

urlpatterns = patterns('',
    url(r'^$', views.front, name='front'),
    url(r'^about/', views.about, name='about'),
)
