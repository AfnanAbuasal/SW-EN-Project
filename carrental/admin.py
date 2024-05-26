from django.contrib import admin
from .models import Vehicle, Customer, Lessor

# Register your models here.

admin.site.register(Vehicle)
admin.site.register(Customer)
admin.site.register(Lessor)
