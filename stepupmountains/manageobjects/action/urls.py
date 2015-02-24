from django.conf.urls import patterns, url

from . import views

urlpatterns = patterns(
	'',
	url(r'add/$', views.add, name='add'),
	url(r'edit/(\d+)/$', views.edit, name='edit'),
	url(r'delete/(\d+)/$', views.delete, name='delete'),
	url(r'deactivate/(\d+)/$', views.deactivate, name='deactivate'),
	url(r'activate/(\d+)/$', views.activate, name='activate'),
	)
