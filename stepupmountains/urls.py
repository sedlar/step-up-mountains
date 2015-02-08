from django.conf.urls import patterns, url

from stepupmountains import views

urlpatterns = patterns(
	'',
	url(r'climb/$', views.climb_object, name='climb_object'),
	url(r'login/$', views.auth_login, name='auth_login'),
	url(r'logout/$', views.auth_logout, name='auth_logout'),
	url(r'add_object/$', views.add_object, name='add_object'),
	url(r'add_object_do/$', views.add_object_do, name='add_object_do'),
	url(r'.*$', views.mountain_list, name='mountain_list'),
	)
