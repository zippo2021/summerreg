from django.conf.urls import patterns, url
from export import views

urlpatterns = patterns('',
    url(r'^exportdb', views.export_database, name='exportdb'),
    url(r'^exportcsv', views.export_csv, name='exportcsv'),
    url(r'^$', views.index, name="index"),
    url(r'^showdb/(?P<id>\d+)', views.apply_user, name='apply_user'), 
    url(r'^showdb', views.create, name='showdb')
)
