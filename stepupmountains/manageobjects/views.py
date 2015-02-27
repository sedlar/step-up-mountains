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
from objects import get_all_objects, get_object_by_id

# Create your views here.
def add(request):
	if request.user.is_authenticated():
		return render(request, 'stepupmountains/add_object_form.html')
	else:
		return HttpResponseRedirect(reverse('stepupmountains:mountain_list'), context)

def edit(request, object_id):
	if request.user.is_authenticated():
		edited_object = get_object_by_id(request.user, object_id)
		if not edited_object:
			return HttpResponseRedirect(reverse('stepupmountains:manageobjects:manageobjects'))
		context = { 'edited_object': edited_object }
		return render(request, 'stepupmountains/add_object_form.html', context)
	else:
		return HttpResponseRedirect(reverse('stepupmountains:mountain_list'))

def manageobjects(request):
	if request.user.is_authenticated():
		objects = get_all_objects(request.user)
		for climbing_object in objects:
			if climbing_object.active:
				climbing_object.link_text = "Deactivate"
			else:
				climbing_object.link_text = "Activate"	
		context = {'active_objects': objects.filter(active=True), 'not_active_objects': objects.filter(active=False)}
		return render(request, 'stepupmountains/manage_objects.html', context)
	else:
		return HttpResponseRedirect(reverse('stepupmountains:mountain_list'))


