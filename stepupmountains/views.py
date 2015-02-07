from django.shortcuts import render
from django.http import HttpResponse
from stepupmountains.models import Mountain
from stepupmountains.models import ClimbingObject
from django.contrib.auth.models import User

# Create your views here.

def mountain_list(request):
	all_mountains = Mountain.objects.order_by('-mountain_elevation');
	all_objects = ClimbingObject.objects.all();
	context = {'mountain_list': all_mountains, 'object_list': all_objects}
	return render(request, 'stepupmountains/mountain_list.html', context)

def climb_object(request):
	return HttpResponse("blah")
	#climbed_object = get_object_or_404(request.POST['climbed_object']
	#if request.user != climbed_object.user
		#HttpResponseForbidden()
	#climb = Climbed(climbed_height=climbed_object.height)
	#climb.save()
	#return HttpResponseRedirect(reverse('stepupmountains:mountain_list')

		
