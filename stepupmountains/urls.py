from django.conf.urls import include, url
from myproject import settings

from stepupmountains import views

urlpatterns = [
	url(r'manage-objects/', include('stepupmountains.manageobjects.urls', namespace="manageobjects")),
	url(r'accounts/', include('stepupmountains.accounts.urls', namespace="accounts")),
	url(r'climb/$', views.climb_object, name='climb_object'),
	url(r'not_so_quickly/$', views.not_so_quickly, name='not_so_quickly'),
	url(r'history/$', views.history, name='history'),
	url(r'statistics/$', views.statistics, name='statistics'),
	url(r'main/(?P<climbed>.*)$', views.mountain_list, name='mountain_list_args'),
    url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),
	url(r'^$', views.mountain_list, name='mountain_list'),
	]
