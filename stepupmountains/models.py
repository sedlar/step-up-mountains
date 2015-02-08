from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.
class Mountain(models.Model):
	name = models.CharField(max_length=200)
	elevation = models.IntegerField()
	comment = models.CharField(max_length=1000)
	
	def __str__(self):
		return self.name + ' (' + str(self.elevation) + ' m.n.m.)'

class ClimbingObject(models.Model):
	user = models.ForeignKey(User)
	name = models.CharField(max_length=200)
	height = models.IntegerField()
	def __str__(self):
		return self.name

class Climbed(models.Model):
	user = models.ForeignKey(User)
	climbed_object = models.ForeignKey(ClimbingObject)
	datetime = models.DateTimeField(default=timezone.now)
	
