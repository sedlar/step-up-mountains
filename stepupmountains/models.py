from django.db import models

# Create your models here.
class Mountains(models.Model):
	mountain_name = models.CharField(max_length=200)
	mountain_elevation = models.IntegerField()
	comment = models.CharField(max_length=1000)
	
	def __str__(self):
		return self.mountain_name + ' (' + str(self.mountain_elevation) + ' m.n.m.)'
