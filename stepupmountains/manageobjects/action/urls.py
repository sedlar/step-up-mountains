from django.conf.urls import patterns, url

from . import views

urlpatterns = patterns(
	'',
	url(r'add/$', views.add, name='add'),
	url(r'edit/$', views.edit, name='edit'),
	url(r'change-order/$', views.changeorder, name='changeorder'),
	url(r'change-active-status/(\d+)/$', views.changeactivestatus, name='changeactivestatus'),
	)
