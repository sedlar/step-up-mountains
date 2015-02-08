from django.contrib import admin
from stepupmountains.models import Mountain
from stepupmountains.models import ClimbingObject
from stepupmountains.models import Climb

class MountainAdmin(admin.ModelAdmin):
	list_display = ['name', 'elevation', 'comment']
	fields = ['name', 'elevation', 'comment']
	search_fields = ['name', 'elevation', 'comment']
	ordering = ['-elevation', 'name']

# Register your models here.
admin.site.register(Mountain, MountainAdmin)
admin.site.register(ClimbingObject)
admin.site.register(Climb)
