from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.
class Mountain(models.Model):
    name = models.CharField(max_length=200)
    elevation = models.IntegerField()
    comment = models.CharField(max_length=1000)
    def is_climbed(self, ascent):
        return ascent >= self.elevation

    def add_climbed_attribute(self, ascent):
        if self.is_climbed(ascent):
            self.climbed = "climbed"
        else:
            self.climbed = ""

    def __str__(self):
        return self.name + ' (' + str(self.elevation) + ' m.n.m.)'

    def __unicode__(self):
        return self.name + ' (' + str(self.elevation) + ' m.n.m.)'

class UserManager(models.Manager):
    def get_user_objects(self, owner):
        return super(UserManager, self).get_queryset().filter(user=owner)

    def get_user_object_by_id(self, owner, object_id):
        selected_objects = super(UserManager, self).get_queryset().filter(user=owner, id=object_id)
        if len(selected_objects)>0:
            return selected_objects[0]
        else:
            return None


class ClimbingObject(models.Model):
    user = models.ForeignKey(User)
    name = models.CharField(max_length=200)
    height = models.FloatField()
    stairs_no = models.IntegerField(default = 0)
    active = models.BooleanField(default=True)
    order = models.IntegerField()
    objects = UserManager()
    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name

class Climb(models.Model):
    user = models.ForeignKey(User)
    climbed_object = models.ForeignKey(ClimbingObject)
    datetime = models.DateTimeField(default=timezone.now)
    objects = UserManager()
    def __str__(self):
        return str(self.user) + ' climbed ' + self.climbed_object.name + ' on ' + str(self.datetime)
