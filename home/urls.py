from django.conf.urls import patterns, url
from django.views.generic.base import RedirectView

from home import views
from setsuhi import settings

s3 = settings.S3_STATIC_URL


woman = RedirectView.as_view(url="http://restaurants.tokyo.grand.hyatt.co.jp/french-kitchen-tokyo/news/woman-experience.html")

blog_redirect = RedirectView.as_view(url='http://setsuhi.blogspot.jp/')

urlpatterns = patterns(
    '',

    # Place the favicon in a standard static location but still conform to an old fashion favicon
    url(r'^favicon\.ico$', RedirectView.as_view(url=s3+'main/icons/favicon.ico'), name='favicon'),

    # For readability I listed this url on a flyer
    url(r'^wom[ae]n(s?)(-?)experience$', woman),

    url(r'^$', views.front, name='front'),
    url(r'^about/', views.about, name='about'),
    url(r'^works/$', views.works, name='works'),
    url(r'^photos/$', views.photos, name='photos'),
    url(r'^schedule/', views.schedule, name='schedule'),
    url(r'^lessons/', views.lessons, name='lessons'),
    url(r'^contact/', views.contact, name='contact'),
    url(r'^blog/', blog_redirect, name='blog'),
)
