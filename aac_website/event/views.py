from django.shortcuts import render
from django.http import HttpResponse
<<<<<<< HEAD
from .models import Event
def indexView(request):
    context = {
    	'events':Event.objects.all()
    }
=======

def indexView(request):
    context = {}
>>>>>>> 2e81c0f2e07b77f4205f065bf060384c69eec4b1
    return render(request,'event/index.html',context)
