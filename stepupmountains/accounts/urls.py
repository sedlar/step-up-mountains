from django.conf.urls import patterns, include, url

from stepupmountains.accounts import views

urlpatterns = patterns(
	'',
	url(r'login/$', views.auth_login, name='auth_login'),
	url(r'logout/$', views.auth_logout, name='auth_logout'),
	url(r'login_failed/$', views.login_failed, name='login_failed'),
	)
