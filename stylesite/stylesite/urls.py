from django.conf.urls import patterns, include, url

from hairstyles import views
import manage
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^hairstyles/', include('hairstyles.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^submit_hairstyle$', views.submit_hairstyle, name='submit_hairstyle'),
    url(r'^search_hairstyle/$', views.search_hairstyle, name='search_hairstyle'),
    url(r'^upload_csv/$', views.upload_csv, name='upload_csv'),
    url(r'^upload_csv$', views.upload_csv, name='upload_csv'),
)
