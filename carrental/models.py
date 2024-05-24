from django.db import models



# Create your models here.

class Lessor(models.Model):
    lessor_id = models.IntegerField(unique= True, auto_created= True, primary_key=True, max_length=64)
    name = models.CharField(max_length=64)
    phone = models.IntegerField(null=False, blank=False, unique=True)
    email = models.EmailField(max_length = 254)
    
    def __str__(self):
        return f"{self.name}"
 

class Vehicle(models.Model):
    vehicle_id = models.IntegerField(unique= True, auto_created= True, primary_key=True, max_length=64)
    lessor_id = models.ForeignKey(Lessor, on_delete= models.CASCADE)
    genre = models.CharField(max_length=64)
    image = models.URLField(blank = True, null = True, max_length=255)
    no_of_seats = models.IntegerField(max_length=8)
    model = models.CharField(max_length=64)
    color = models.CharField(max_length=64)
    mileage = models.FloatField(max_length=64)
    transmission = models.CharField(max_length=50)
    no_of_doors = models.IntegerField(max_length = 8)
    fuel_policy = models.CharField(max_length=50)
    price_per_day = models.IntegerField(max_length=64)
    
    def __str__(self):
        return f"{self.model}"
    
   
class Customer(models.Model):
    customer_id = models.IntegerField(unique= True, auto_created= True, primary_key=True, max_length=64)
    name = models.CharField(max_length=64)
    phone = models.IntegerField(null=False, blank=False, unique=True)
    email = models.EmailField(max_length = 254)
    
    def __str__(self):
        return f"{self.name}"
    
    
   
class Renting(models.Model):
    rent_id= models.IntegerField(unique= True, auto_created= True, primary_key=True, max_length=64)
    vehicle_id = models.OneToOneField(Vehicle, on_delete= models.CASCADE)
    customer_id = models.OneToOneField(Customer, on_delete= models.CASCADE)
    
    def __str__(self):
        return f"{self.rent_id}"
    


    

