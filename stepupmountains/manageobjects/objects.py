from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from stepupmountains.models import ClimbingObject

def get_max_object_order(user):
	all_objects = []
	if user.is_authenticated():
		latest_object = ClimbingObject.objects.get_user_objects(user).extra(order_by = ['-order']).first()
	if latest_object:
		return latest_object.order
	else:
		return 0

def get_all_objects(user):
	all_objects = []
	if user.is_authenticated():
		all_objects = ClimbingObject.objects.get_user_objects(user).extra(order_by = ['-active', 'order'])
	return all_objects

def get_all_active_objects(user):
	all_objects = []
	if user.is_authenticated():
		all_objects = ClimbingObject.objects.get_user_objects(user).filter(active=True).extra(order_by = ['order'])
	return all_objects


def get_object_by_id(user, object_id):
	if user.is_authenticated():
		return ClimbingObject.objects.get_user_object_by_id(user, object_id)	
	return null
	
