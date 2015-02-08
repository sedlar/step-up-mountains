from django.conf.urls import patterns, url

from stepupmountains import views

urlpatterns = patterns(
	'',
	url(r'climb/$', views.climb_object, name='climb_object'),
	url(r'login/$', views.auth_login, name='auth_login'),
	url(r'logout/$', views.auth_logout, name='auth_logout'),
	url(r'.*$', views.mountain_list, name='mountain_list'),
	)
