from django.shortcuts import render
from django.http import HttpResponse, HttpResponseBadRequest

from rockseven.models import Received

# Create your views here.

def index(request):
    received_messages = Received.objects.all()
    
    return HttpResponse("yo")

def receive(request):
    if request.POST:
        message = Received(
            imei = request.POST.imei,
            sequence_number = request.POST.momsn,
            timestamp_transmit = request.POST.transmit_time,
            latitude = request.POST.iridium_latitude,
            longitude = request.POST.iridium_longitude,
            circular_error_probable = request.POST.iridium_cep,
            data = request.POST.data
        )
        
        message.save()
        
        return HttpResponse()
    
    return HttpResponseBadRequest()
