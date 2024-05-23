from django.shortcuts import render
from .models import Lessor, Vehicle, Renting, Customer
from django.http import  HttpResponse, HttpResponseRedirect


# Create your views here.

def index(request):
    return render(request, "carrental/index.html",{
        "vehicle" : Vehicle.objects.all()})