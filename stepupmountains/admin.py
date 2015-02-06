from django.contrib import admin
from stepupmountains.models import Mountain

class MountainAdmin(admin.ModelAdmin):
	fields = ['mountain_name', 'mountain_elevation', 'mountain_comment']

# Register your models here.
admin.site.register(Mountain, MountainAdmin)
