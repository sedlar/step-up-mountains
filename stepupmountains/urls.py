from django.conf.urls import patterns, url

from stepupmountains import views

urlpatterns = patterns('', url(r'^$', views.mountain_list, name='mountain_list'),)
