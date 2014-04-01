from django.conf.urls import patterns, url

from dashboard import views

urlpatterns = patterns('',
    url(r'^$', views.dash_index, name='dash_index'),
    url(r'^summer_registration$', views.summer_registration, name='summer_registration'),
        
        )