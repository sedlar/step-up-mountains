from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from stepupmountains.models import ClimbingObject

def get_all_objects(user):
	all_objects = []
	if user.is_authenticated():
		all_objects = ClimbingObject.objects.get_user_objects(user)
	return all_objects
