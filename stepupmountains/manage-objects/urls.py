from django.conf.urls import patterns, include, url

from . import views

urlpatterns = patterns(
	'',
	url(r'/action', include('stepupmountains.manage-objects.action.urls', namespace="action")),
	url(r'add/$', views.add, name='add'),
	url(r'edit/(\d+)/$', views.edit, name='edit'),
	url(r'.*', views.list_all, name='list-all'),
	)
