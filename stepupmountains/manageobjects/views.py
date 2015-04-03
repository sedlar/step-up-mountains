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
import re
from datetime import timedelta
from objects import get_all_objects, get_object_by_id, get_max_object_order
from django.views.decorators.http import require_GET, require_POST
from django.views.decorators.http import require_http_methods
from django.contrib.auth.decorators import login_required
from stepupmountains.manageobjects.climbing_object_form import ClimbingObjectForm

# Create your views here.
@require_http_methods(["GET", "POST"])
@login_required
def add(request):
    if request.method == 'POST':
        form = ClimbingObjectForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            object_order = get_max_object_order(request.user) + 1
            climbing_object = ClimbingObject(user = request.user, name = form.cleaned_data['name'], height = form.cleaned_data['height'], stairs_no = form.cleaned_data['stairs_no'], order = object_order)
            climbing_object.save()

            return HttpResponseRedirect(reverse('stepupmountains:manageobjects:manageobjects'))

    # if a GET (or any other method) we'll create a blank form
    else:
        form = ClimbingObjectForm()
    return render(request, 'stepupmountains/add_object_form.html', {'form': form})

@require_http_methods(["GET", "POST"])
@login_required
def edit(request, object_id = None):
    if request.method == 'POST':
        form = ClimbingObjectForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            object_order = get_max_object_order(request.user) + 1
            climbing_object = get_object_by_id(request.user, form.cleaned_data['object_id'])
            if climbing_object:
                climbing_object.name = form.cleaned_data['name']
                climbing_object.height = form.cleaned_data['height']
                climbing_object.stairs_no = form.cleaned_data['stairs_no']
                climbing_object.save()

            return HttpResponseRedirect(reverse('stepupmountains:manageobjects:manageobjects'))

    # if a GET (or any other method) we'll create a blank form
    else:
        edited_object = get_object_by_id(request.user, object_id)
        if edited_object:
            data = {'name': edited_object.name, 'object_id': edited_object.id, 'height': edited_object.height, 'stairs_no': edited_object.stairs_no}
            form = ClimbingObjectForm(initial = data)
        else:
            return HttpResponseRedirect(reverse('stepupmountains:manageobjects:manageobjects'))

    return render(request, 'stepupmountains/add_object_form.html', {'form': form, 'edit': True})


@require_GET
@login_required
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

@require_GET
@login_required
def changeactivestatus(request, object_id):
	changed_object = get_object_by_id(request.user, object_id)
	if changed_object.active:
		changed_object.active = False
		#changed_object.order = get_max_object_order(request.user) + 1
	else:
		changed_object.active = True
	changed_object.save()
	return HttpResponseRedirect(reverse('stepupmountains:manageobjects:manageobjects'))

@require_http_methods(["GET", "POST"])
@login_required
def changeorder(request):
	if request.method == 'GET':
		return HttpResponseRedirect(reverse('stepupmountains:manageobjects:manageobjects'))
	for order_data in request.POST.items():
		if re.match("^[0-9]+$", order_data[0]):
			changed_object = get_object_by_id(request.user, order_data[0])
			if re.match("^[0-9]+$", order_data[1]):
				changed_object.order = order_data[1]
				changed_object.save()
			else:
				changed_object.order = 9999999
				changed_object.save()
			
	return HttpResponseRedirect(reverse('stepupmountains:manageobjects:manageobjects'))

