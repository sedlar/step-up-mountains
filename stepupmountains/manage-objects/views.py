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

# Create your views here.
def add(request):
	if request.user.is_authenticated():
		return render(request, 'stepupmountains/add_object_form.html')
	else:
		return HttpResponseRedirect(reverse('stepupmountains:mountain_list'))

def edit(request):
	return HttpResponseForbidden('Not implemented')

def list_all(request):
	return HttpResponseForbidden('Not implemented')

