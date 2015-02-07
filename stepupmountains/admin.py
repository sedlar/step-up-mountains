from django.contrib import admin
from stepupmountains.models import Mountain
from stepupmountains.models import Object

class MountainAdmin(admin.ModelAdmin):
	list_display = ['mountain_name', 'mountain_elevation', 'mountain_comment']
	fields = ['mountain_name', 'mountain_elevation', 'mountain_comment']
	search_fields = ['mountain_name', 'mountain_elevation', 'mountain_comment']
	ordering = ['-mountain_elevation', 'mountain_name']

# Register your models here.
admin.site.register(Mountain, MountainAdmin)
admin.site.register(Object)
