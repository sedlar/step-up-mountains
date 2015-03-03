from django.views.decorators.http import require_GET, require_POST
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views.decorators.http import require_http_methods
from django.shortcuts import render

@require_GET
def auth_logout(request):
	logout(request)
	return HttpResponseRedirect(reverse('stepupmountains:mountain_list'))
