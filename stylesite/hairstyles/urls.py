from django.conf.urls import patterns, url

from hairstyles import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^(?P<hairstyle_id>\d+)/$', views.detail, name='detail'),
    url(r'^(?P<hairstyle_id>\d+)/zoom/$', views.zoom, name='zoom'),    
    url(r'^add_style/$', views.add_style, name='add_style'),
    url(r'^(?P<hairstyle_id>\d+)/delete/$', views.delete, name='delete'),
    url(r'^(?P<hairstyle_id>\d+)/update/$', views.update, name='update'),
    url(r'^search/$', views.search, name='search'),
    url(r'^next_search/$', views.next_search, name='next_search'),
    url(r'^next_search$', views.next_search, name='next_search'),
    url(r'^last_search/$', views.last_search, name='last_search'),
    url(r'^last_search$', views.last_search, name='last_search'),
    url(r'^csv/$', views.handling_csv, name='csv'),
    url(r'^upload_csv/$', views.upload_csv, name='upload_csv'),
    url(r'^upload_csv$', views.upload_csv, name='upload_csv'),
    url(r'^clear_all/$', views.clear_all, name='clear_all'),
    url(r'^clear_all$', views.clear_all, name='clear_all'),    
)