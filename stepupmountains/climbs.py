from stepupmountains.models import Climb
from math import floor
from Queue import Queue
from datetime import timedelta

def get_all_climbs(user):
	all_climbs = []
	if user.is_authenticated():
		all_climbs = Climb.objects.get_user_objects(user)
	return all_climbs


def get_total_ascent(user):
	total_climbed=0
	all_climbs = get_all_climbs(user)
	for climb in all_climbs:
		total_climbed += climb.climbed_object.height
	return floor(total_climbed)

def get_total_stairs(user):
	total_stairs=0
	all_climbs = get_all_climbs(user)
	for climb in all_climbs:
		total_stairs += climb.climbed_object.stairs_no
	return total_stairs

def get_fastest_climb(climbs, highest_mountain):
    fastest_climb = timedelta.max
    actual_climb_height = 0
    actual_climb = Queue()

    for climb in climbs:
        actual_climb.put(climb)
        actual_climb_height += climb.climbed_object.height

        while actual_climb_height >= highest_mountain.elevation:
            first_climb=actual_climb.get()
            climb_time = climb.datetime-first_climb.datetime
            actual_climb_height -= first_climb.climbed_object.height
            if climb_time < fastest_climb:
                fastest_climb = climb_time
    return fastest_climb

def format_fastest_climb(fastest_climb):
    if fastest_climb == timedelta.max:
        return "N/A"
    s = int(fastest_climb.total_seconds())
    days, remainder = divmod(s, 86400)
    hours, remainder = divmod(remainder, 3600)
    minutes, seconds = divmod(remainder, 60)
    str_fastest_climb = '%s days %s hours %s minutes' % (days, hours, minutes)
    return str_fastest_climb


