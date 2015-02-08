from django.conf.urls import patterns, url

from stepupmountains import views

urlpatterns = patterns(
	'',
	url(r'climb/$', views.climb_object, name='climb_object'),
	url(r'.*$', views.mountain_list, name='mountain_list'),
	)
