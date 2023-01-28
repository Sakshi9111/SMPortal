from django.shortcuts import render, redirect
from .models import Sites

# Create your views here.
from django.http import HttpResponse
from . import views

#def index(request):
    #return HttpResponse ("Hello World! This is a first page of django application")

def iissite(request):
    all_sites = Sites.objects.all()
    return render(request, 'datatables/index.html', {'all_sites': all_sites})


def home(request):
	return render(request, 'datatables/home.html', {})   