from django.conf.urls import patterns, include, url
import django.contrib.auth.views
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import CreateView
from django.core.urlresolvers import reverse

APEND_SLASH = True
urlpatterns = patterns(
    '',
    url(r'^login/$', 'django.contrib.auth.views.login', {'template_name': 'stepupmountains/login.html'}, name='login'),
    url(r'^logout/$', 'django.contrib.auth.views.logout', {'next_page': 'stepupmountains:mountain_list'}),
    url(r'^change-password/$', 'django.contrib.auth.views.password_change', {'template_name': 'stepupmountains/changepassword.html', 'post_change_redirect': 'stepupmountains:accounts:change_password_done'}
        , name='change_password'),
    url(r'^change-password-done/$', 'django.contrib.auth.views.password_change_done', {'template_name': 'stepupmountains/changepassworddone.html'},
        name='change_password_done'),
    url(r'^register/$', CreateView.as_view(
            template_name='stepupmountains/register.html',
            form_class=UserCreationForm,
            success_url='/accounts/login/')
        , name='register'),
    )
