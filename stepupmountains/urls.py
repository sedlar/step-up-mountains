from django.conf.urls import patterns, include, url

from stepupmountains import views

urlpatterns = patterns(
	'',
	url(r'manage-objects/', include('stepupmountains.manageobjects.urls', namespace="manageobjects")),
	url(r'accounts/', include('stepupmountains.accounts.urls', namespace="accounts")),
	url(r'climb/$', views.climb_object, name='climb_object'),
	url(r'not_so_quickly/$', views.not_so_quickly, name='not_so_quickly'),
	url(r'.*$', views.mountain_list, name='mountain_list'),
	)
