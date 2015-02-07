from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Mountain(models.Model):
	mountain_name = models.CharField(max_length=200)
	mountain_elevation = models.IntegerField()
	mountain_comment = models.CharField(max_length=1000)
	
	def __str__(self):
		return self.mountain_name + ' (' + str(self.mountain_elevation) + ' m.n.m.)'

class Object(models.Model):
	user = models.ForeignKey(User)
	object_name = models.CharField(max_length=200)
	height = models.IntegerField()

class Climbed(models.Model):
	user = models.ForeignKey(User)
	climbed_object = models.ForeignKey(Object)
	
