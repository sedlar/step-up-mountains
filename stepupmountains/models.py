from django.db import models

# Create your models here.
class Mountain(models.Model):
	mountain_name = models.CharField(max_length=200)
	mountain_elevation = models.IntegerField()
	comment = models.CharField(max_length=1000)
