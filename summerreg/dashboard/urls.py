from django.conf.urls import patterns, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns 

from dashboard import views

urlpatterns = patterns('',
    url(r'^$', views.dash_index, name='dash_index'),
    url(r'^summer_registration$', views.summer_registration, name='summer_registration'),
    url(r'^user_data', views.user_data_viewer, name='user_data'), 
    url(r'^doc_type_select', views.doc_type_select, name='doc_type_select'),
    url(r'^doc_info', views.doc_info, name='doc_info'),          
    url(r'^admin_events/apply/(?P<event_id>\d+)/(?P<user_id>\w+)/(?P<p_type>[0-9]{1})', views.admin_events_apply, name="admin_events_apply"),
    url(r'^admin_events/disapply/(?P<event_id>\d+)/(?P<user_id>\w+)', views.admin_events_disapply, name="admin_events_disapply"),
    url(r'admin_events/show/(?P<event_id>\d+)', views.admin_events_show, name='admin_events_show'),
    url(r'^admin_events', views.admin_events_main, name='admin_events_main'),
    url(r'^user_events/information/(?P<filename>\w+.*)',views.user_events_information_file, name='user_events_information_file'), 
    url(r'^user_events/request/(?P<event_id>\d+)', views.user_events_request, name='user_events_request'),
    url(r'^user_events/undo/(?P<event_id>\d+)', views.user_events_undo, name='user_events_undo'),
    url(r'^user_events', views.user_events_main, name='user_events_main'),
    url(r'^view_profile', views.view_profile, name='view_profile'),
    )

