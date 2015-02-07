from django.shortcuts import render
from django.http import HttpResponse
from stepupmountains.models import Mountain

# Create your views here.

def mountain_list(request):
	all_mountains = Mountain.objects.order_by('-mountain_elevation');
	context = {'mountain_list': all_mountains}
	return render(request, 'stepupmountains/mountain_list.html', context)
