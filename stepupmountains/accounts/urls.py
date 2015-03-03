from django.conf.urls import patterns, include, url

from stepupmountains.accounts import views
import django.contrib.auth.views

APEND_SLASH = True
urlpatterns = patterns(
	'',
	url(r'login/$', 'django.contrib.auth.views.login', {'template_name': 'stepupmountains/login.html'}),
	url(r'logout/$', views.auth_logout, name='auth_logout'),
	)
