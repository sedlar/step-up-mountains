from django.conf.urls import patterns, include, url
from stepupmountains.manageobjects import views

urlpatterns = patterns(
	'',
	url(r'add/$', views.add, name='add'),
	url(r'edit/$', views.edit, name='edit'),
	url(r'edit/(\d+)/$', views.edit, name='edit'),
	url(r'change-order/$', views.changeorder, name='changeorder'),
	url(r'change-active-status/(\d+)/$', views.changeactivestatus, name='changeactivestatus'),
	url(r'.*', views.manageobjects, name='manageobjects'),
	)
