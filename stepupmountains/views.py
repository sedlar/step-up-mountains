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

# Create your views here.

def login_failed(request):
	return render(request, 'stepupmountains/login_failed.html')

def auth_logout(request):
	logout(request)
	return HttpResponseRedirect(reverse('stepupmountains:mountain_list'))

def auth_login(request):
	user = authenticate(username=request.POST['username'], password=request.POST['password'])
	if user is not None:
		if user.is_active:
			login(request, user)
			if request.META['HTTP_REFERER']:
				return HttpResponseRedirect(request.META['HTTP_REFERER'])
			else:
				return HttpResponseRedirect(reverse('stepupmountains:mountain_list'))
				
	return HttpResponseRedirect(reverse('stepupmountains:login_failed'))

def mountain_list(request):
	all_mountains = Mountain.objects.order_by('-elevation');
	all_objects = []
	all_climbs = []
	total_climbed=0
	if request.user.is_authenticated():
		all_objects = ClimbingObject.objects.get_user_objects(request.user)
		all_climbs = Climb.objects.get_user_objects(request.user)
		for climb in all_climbs:
			total_climbed += climb.climbed_object.height
	for mountain in all_mountains:
		mountain.climbed = Mountain.is_climbed(mountain, total_climbed)
	context = {'mountain_list': all_mountains, 'object_list': all_objects, 'total_climbed': total_climbed}
	return render(request, 'stepupmountains/mountain_list.html', context)

def climb_object(request):
	if not request.user.is_authenticated():
		return HttpResponseForbidden('Login before climbing')	
	climbed_object = get_object_or_404(ClimbingObject, pk=request.POST['climbed_object'])
	if request.user != climbed_object.user:
		return HttpResponseForbidden('You are not allowed to climb this object')

	climb = Climb(user=request.user, climbed_object=climbed_object)
	climb.save()
	return HttpResponseRedirect(reverse('stepupmountains:mountain_list'))
