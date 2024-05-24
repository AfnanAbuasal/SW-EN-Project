from django.shortcuts import render
from .models import Lessor, Vehicle, Renting, Customer



# Create your views here.

def index(request):
    return render(request, "carrental/index.html",{
        "vehicles" : Vehicle.objects.all()})