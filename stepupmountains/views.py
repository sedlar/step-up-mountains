from django.shortcuts import render
from django.http import HttpResponse
from stepupmountains.models import Mountain
from stepupmountains.models import ClimbingObject
from stepupmountains.models import Climb
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

# Create your views here.

def mountain_list(request):
	all_mountains = Mountain.objects.order_by('-elevation');
	all_objects = ClimbingObject.objects.all();
	total_climbed=0
	all_climbs = Climb.objects.all();
	for climb in all_climbs:
		total_climbed += climb.climbed_object.height

	context = {'mountain_list': all_mountains, 'object_list': all_objects, 'total_climbed': total_climbed}
	return render(request, 'stepupmountains/mountain_list.html', context)

def climb_object(request):
	climbed_object = get_object_or_404(ClimbingObject, pk=request.POST['climbed_object'])
	if request.user != climbed_object.user:
		return HttpResponseForbidden('You are not allowed to climb this object')

	climb = Climb(user=request.user, climbed_object=climbed_object)
	climb.save()
	return HttpResponseRedirect(reverse('stepupmountains:mountain_list'))
