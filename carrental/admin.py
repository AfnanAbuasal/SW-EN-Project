from django.contrib import admin
from .models import Vehicle, Customer, Renting, Lessor

# Register your models here.

admin.site.register(Vehicle)
admin.site.register(Customer)
admin.site.register(Renting)
admin.site.register(Lessor)
