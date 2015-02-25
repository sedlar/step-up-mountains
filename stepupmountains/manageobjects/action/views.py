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
from objects import get_object_by_id, get_max_object_order

# Create your views here.

def add(request):
	if not request.user.is_authenticated():
		return HttpResponseForbidden('You need to log in before adding objects')
	object_name = request.POST['object_name']
	object_height = request.POST['object_height']
	if not object_name or not re.match("^[0-9]+(\.[0-9]+)?$", object_height):
		return HttpResponseRedirect(reverse('stepupmountains:manageobjects:manageobjects'))
	object_order = get_max_object_order(request.user) + 1
	climbing_object = ClimbingObject(user = request.user, name = object_name, height = object_height, order = object_order)
	climbing_object.save()
	return HttpResponseRedirect(reverse('stepupmountains:manageobjects:manageobjects'))

def edit(request):
	if not request.user.is_authenticated():
		return HttpResponseForbidden('You need to log in before editing objects')
	object_name = request.POST['object_name']
	object_height = request.POST['object_height']
	object_id = request.POST['object_id']
	if not object_name or not re.match("^[0-9]+(\.[0-9]+)?$", object_height) or not re.match("^[0-9]+$", object_id):
		return HttpResponseRedirect(reverse('stepupmountains:manageobjects:manageobjects'))
	climbing_object = get_object_by_id(request.user, object_id)
	climbing_object.name = object_name
	climbing_object.height = object_height
	climbing_object.save()
	return HttpResponseRedirect(reverse('stepupmountains:manageobjects:manageobjects'))

def delete(request):
	return HttpResponseForbidden('Not implemented')

def activate(request):
	return HttpResponseForbidden('Not implemented')

def deactivate(request):
	return HttpResponseForbidden('Not implemented')


