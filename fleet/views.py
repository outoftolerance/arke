from django.shortcuts import render
from django.http import HttpResponse

from fleet.models import Vehicle

# Create your views here.

def index(request):
    vehicles = Vehicle.objects.all()
    
    return HttpResponse("Hi there")
