from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from stepupmountains.models import ClimbingObject

def get_all_objects(user):
	all_objects = []
	if user.is_authenticated():
		all_objects = ClimbingObject.objects.get_user_objects(user)
	return all_objects

def get_object_by_id(user, object_id):
	if user.is_authenticated():
		return ClimbingObject.objects.get_user_object_by_id(user, object_id)	
	return null
	
