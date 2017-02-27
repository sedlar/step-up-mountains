from django.shortcuts import render
from django.http import HttpResponse
from stepupmountains.models import Mountain
from stepupmountains.models import ClimbingObject
from stepupmountains.models import Climb
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.utils import timezone
import datetime
from datetime import timedelta
import re
from stepupmountains.manageobjects.objects import get_object_by_id, get_all_active_objects
from django.contrib.auth.decorators import login_required
from stepupmountains.climbs import get_total_ascent, get_all_climbs, get_total_stairs, get_fastest_climb, format_fastest_climb
from django.views.decorators.http import require_GET, require_POST
from django.views.decorators.http import require_http_methods
from stepupmountains.mountains import add_climbed_attribute_to_all
import math

# Create your views here.

@require_GET
@login_required
def not_so_quickly(request):
    return render(request, 'stepupmountains/not_so_quickly.html')

@require_GET
def mountain_list(request, climbed = None):
    all_mountains = Mountain.objects.order_by('-elevation');
    if len(all_mountains):
        highest_mountain_elevation = all_mountains[0].elevation
    else:
        highest_mountain_elevation = 9999999999999999999
    all_objects = get_all_active_objects(request.user)
    total_climbed = get_total_ascent(request.user) % highest_mountain_elevation
    add_climbed_attribute_to_all(all_mountains, total_climbed)

    next_mountains = all_mountains.filter(elevation__gt = total_climbed).order_by('elevation')
    if len(next_mountains) == 0:
        next_mountain = Mountain(name = "None", elevation = 0)
    else:
        next_mountain = next_mountains[0]

    climbed_mountains = all_mountains.filter(elevation__lte = total_climbed).order_by('-elevation')
    if len(climbed_mountains) == 0:
        reached_mountain = Mountain(name = "None", elevation = 0)
    else:
        reached_mountain = climbed_mountains[0]

    remains_to_climb = next_mountain.elevation - total_climbed
    context = {'mountain_list': all_mountains, 'object_list': all_objects, 'total_climbed': int(total_climbed), 'reached_mountain': reached_mountain, 'next_mountain': next_mountain.name, 'remains_to_climb': int(remains_to_climb), 'climbed': climbed}
    return render(request, 'stepupmountains/mountain_list.html', context)

@require_http_methods(['GET', 'POST'])
@login_required
def climb_object(request):
    if request.method == 'GET':
        return HttpResponseRedirect(reverse('stepupmountains:mountain_list'))
		
    if not re.match("^[0-9]+$", request.POST['climbed_object']):
        return HttpResponseRedirect(reverse('stepupmountains:mountain_list'))
		
    climbed_object = get_object_by_id(request.user, request.POST['climbed_object'])
    if request.user != climbed_object.user:
        return HttpResponseForbidden('You are not allowed to climb this object')

    latest_climb = get_all_climbs(request.user).extra(order_by = ['-datetime']).first()
    if latest_climb:
        if latest_climb.datetime + datetime.timedelta(minutes=0) > timezone.now():
            return HttpResponseRedirect(reverse('stepupmountains:not_so_quickly'))
			
    climb = Climb(user=request.user, climbed_object=climbed_object)
    climb.save()
    return HttpResponseRedirect(reverse('stepupmountains:mountain_list_args', kwargs={'climbed': climbed_object.name}))

@require_GET
@login_required
def history(request):
    climbs = get_all_climbs(request.user).order_by('-datetime')
    context = {'climbs': climbs}
    return render(request, 'stepupmountains/history.html', context)

@require_GET
@login_required
def statistics(request):
    total_ascent = get_total_ascent(request.user)
    total_stairs = get_total_stairs(request.user)
    highest_mountain = Mountain.objects.order_by('-elevation').first();

    first_climbed_date = get_all_climbs(request.user).order_by('datetime').first()
    if first_climbed_date is None:
        first_climbed = 'Never'
        average_climb = 'N/A'
        average_active_climb = 'N/A'
        highest_mountain_climbed = 'N/A'
        str_fastest_climb = 'N/A'
    else:
        first_climbed = first_climbed_date.datetime
        total_days = (timezone.now().date()-first_climbed.date()).days+1
        average_climb = round(total_ascent/total_days, 1)

        climbing_days = get_all_climbs(request.user).values('datetime')
        active_days = set()
        for d in climbing_days:
            active_days.add(d['datetime'].date())
    
        num_active_days = len(active_days)
        average_active_climb = round(total_ascent/num_active_days, 1)
        highest_mountain_climbed = int(math.floor(total_ascent/highest_mountain.elevation))
        fastest_climb = get_fastest_climb(get_all_climbs(request.user).order_by('datetime'), highest_mountain)
        str_fastest_climb = format_fastest_climb(fastest_climb)
        
    context = {'total_ascent': total_ascent, 'first_climbed': first_climbed, 'average_climb': average_climb, 'average_active_climb': average_active_climb, 'total_stairs': total_stairs, 'highest_mountain_climbed': highest_mountain_climbed, 'fastest_climb': str_fastest_climb}
    return render(request, 'stepupmountains/statistics.html', context)
