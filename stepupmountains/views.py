from django.shortcuts import render
from django.http import HttpResponse
from stepupmountains.models import Mountain
from stepupmountains.models import ClimbingObject
from stepupmountains.models import Climb
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from django.http import HttpResponseForbidden
from django.core.urlresolvers import reverse
from django.contrib.auth import authenticate, login, logout
from django.utils import timezone
import datetime
from datetime import timedelta
import re
from objects import get_object_by_id, get_all_active_objects
from django.contrib.auth.decorators import login_required
from stepupmountains.climbs import get_total_ascent
from django.views.decorators.http import require_GET, require_POST

# Create your views here.

@require_GET
def not_so_quickly(request):
	return render(request, 'stepupmountains/not_so_quickly.html')

@require_GET
def login_failed(request):
	return render(request, 'stepupmountains/login_failed.html')

@require_GET
def auth_logout(request):
	logout(request)
	return HttpResponseRedirect(reverse('stepupmountains:mountain_list'))

@require_POST
def auth_login(request):
	user = authenticate(username=request.POST['username'], password=request.POST['password'])
	if user is not None:
		if user.is_active:
			login(request, user)
			if request.META['HTTP_REFERER'] and request.META['HTTP_REFERER'] == reverse('stepupmountains:login_failed'):
				return HttpResponseRedirect(request.META['HTTP_REFERER'])
			else:
				return HttpResponseRedirect(reverse('stepupmountains:mountain_list'))
				
	return HttpResponseRedirect(reverse('stepupmountains:login_failed'))

@require_GET
def mountain_list(request):
	all_mountains = Mountain.objects.order_by('-elevation');
	all_objects = get_all_active_objects(request.user)
	total_climbed = get_total_ascent(request.user)
	for mountain in all_mountains:
		mountain.climbed = Mountain.is_climbed(mountain, total_climbed)
	context = {'mountain_list': all_mountains, 'object_list': all_objects, 'total_climbed': total_climbed}
	return render(request, 'stepupmountains/mountain_list.html', context)

@require_POST
def climb_object(request):
	if not request.user.is_authenticated():
		return HttpResponseForbidden('Login before climbing')	
	if not re.match("^[0-9]+$", request.POST['climbed_object']):
		return HttpResponseRedirect(reverse('stepupmountains:mountain_list'))
		
	climbed_object = get_object_by_id(request.user, request.POST['climbed_object'])
	if request.user != climbed_object.user:
		return HttpResponseForbidden('You are not allowed to climb this object')

	latest_climb = get_all_climbs(request.user).extra(order_by = ['-datetime']).first()
	if latest_climb:
		if latest_climb.datetime + datetime.timedelta(minutes=1) > timezone.now():
			return HttpResponseRedirect(reverse('stepupmountains:not_so_quickly'))
			
	climb = Climb(user=request.user, climbed_object=climbed_object)
	climb.save()
	return HttpResponseRedirect(reverse('stepupmountains:mountain_list'))
