from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.
class Mountain(models.Model):
	name = models.CharField(max_length=200)
	elevation = models.IntegerField()
	comment = models.CharField(max_length=1000)
	def is_climbed(self, ascent):
		if ascent >= self.elevation:
			return 'Climbed'
		return 'NotClimbed'
	
	def __str__(self):
		return self.name + ' (' + str(self.elevation) + ' m.n.m.)'

class UserManager(models.Manager):
    def get_user_objects(self, logged_user):
        return super(UserManager, self).get_query_set().filter(user=logged_user)

class ClimbingObject(models.Model):
	user = models.ForeignKey(User)
	name = models.CharField(max_length=200)
	height = models.IntegerField()
	objects = UserManager()
	def __str__(self):
		return self.name

class Climb(models.Model):
	user = models.ForeignKey(User)
	climbed_object = models.ForeignKey(ClimbingObject)
	datetime = models.DateTimeField(default=timezone.now)
	objects = UserManager()
	def __str__(self):
		return str(self.user) + ' climbed ' + self.climbed_object.name + ' on ' + str(self.datetime)
	
