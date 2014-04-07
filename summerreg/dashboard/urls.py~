from django.conf.urls import patterns, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns 

from dashboard import views

urlpatterns = patterns('',
    url(r'^$', views.dash_index, name='dash_index'),
    url(r'^summer_registration$', views.summer_registration, name='summer_registration'),
    url(r'^user_data', views.user_data_viewer, name='user_data'), 
    url(r'^doc_type_select', views.doc_type_select, name='doc_type_select'),
    url(r'^doc_info', views.doc_info, name='doc_info'),       
        )
urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
