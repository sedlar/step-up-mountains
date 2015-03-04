from django.conf.urls import patterns, include, url
from stepupmountains.accounts import views
import django.contrib.auth.views
from django.contrib.auth.forms import UserCreationForm

APEND_SLASH = True
urlpatterns = patterns(
	'',
	url(r'login/$', 'django.contrib.auth.views.login', {'template_name': 'stepupmountains/login.html'}, name='login'),
	url(r'logout/$', 'django.contrib.auth.views.logout', {'next_page': 'stepupmountains:mountain_list'}),
	#url(r'register/$', 'django.contrib.auth.views.login', {'authentication_form': UserCreationForm, 'template_name': 'stepupmountains/register.html'}, name='register'),
	)
