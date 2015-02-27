from django.conf.urls import patterns, include, url
from stepupmountains.manageobjects import views

urlpatterns = patterns(
	'',
	url(r'action/', include('stepupmountains.manageobjects.action.urls', namespace="action")),
	url(r'add/$', views.add, name='add'),
	url(r'edit/(\d+)/$', views.edit, name='edit'),
	url(r'.*', views.manageobjects, name='manageobjects'),
	)
