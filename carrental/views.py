from django.shortcuts import render, reverse
from .models import Lessor, Vehicle, Customer
from django.http import HttpResponse, HttpResponseRedirect



# Create your views here.

def index(request):
    return render(request, "carrental/index.html",{
        "vehicles" : Vehicle.objects.all()})
    
def car_det(request, vehicle_id):
    vehicle=Vehicle.objects.get(id=vehicle_id)
    return render(request, "carrental/car_details.html", {
        "vehicle" : vehicle,
        "customers" : Customer.objects.all(),
        }
    )
    
    """""
    No need for this for now
def rent(request, vehicle_id):
    if request.method=="POST":
        customer_id = int(request.POST["customer"])
        customer = Customer.objects.get(id = customer_id)
        vehicle = Vehicle.objects.get(id = vehicle_id)
        vehicle.customer_id.add(customer)
        
        return HttpResponseRedirect(reverse("vehicle", args=(vehicle.id,)))
    
"""

        
        
        
    
    


