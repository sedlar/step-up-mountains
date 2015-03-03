from django.views.decorators.http import require_GET, require_POST
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views.decorators.http import require_http_methods
from django.shortcuts import render

@require_GET
def login_failed(request):
	return render(request, 'stepupmountains/login_failed.html')

@require_GET
def auth_logout(request):
	logout(request)
	return HttpResponseRedirect(reverse('stepupmountains:mountain_list'))

@require_http_methods(["GET", "POST"])
def auth_login(request):
	if request.method == "GET":
		return render(request, 'stepupmountains/login.html')
	else:
		user = authenticate(username=request.POST['username'], password=request.POST['password'])
		if user is not None:
			if user.is_active:
				login(request, user)
				if request.META['HTTP_REFERER'] and request.META['HTTP_REFERER'] == reverse('stepupmountains:accounts:login_failed'):
					return HttpResponseRedirect(request.META['HTTP_REFERER'])
				else:
					return HttpResponseRedirect(reverse('stepupmountains:mountain_list'))
					
		return HttpResponseRedirect(reverse('stepupmountains:accounts:login_failed'))
