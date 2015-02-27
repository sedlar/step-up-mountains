from django.conf.urls import patterns, include, url

from stepupmountains import views

urlpatterns = patterns(
	'',
	url(r'manage-objects/', include('stepupmountains.manageobjects.urls', namespace="manageobjects")),
	url(r'climb/$', views.climb_object, name='climb_object'),
	url(r'login/$', views.auth_login, name='auth_login'),
	url(r'logout/$', views.auth_logout, name='auth_logout'),
	url(r'login_failed/$', views.login_failed, name='login_failed'),
	url(r'not_so_quickly/$', views.not_so_quickly, name='not_so_quickly'),
	url(r'.*$', views.mountain_list, name='mountain_list'),
	)
