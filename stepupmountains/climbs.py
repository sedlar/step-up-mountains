from stepupmountains.models import Climb
from math import floor

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

