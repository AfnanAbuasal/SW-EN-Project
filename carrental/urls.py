from django.urls import path
from . import views


urlpatterns = [
    path("", views.index, name="index"),
    path("<int:vehicle_id>", views.car_det, name="vehicle"),
    path("<int:vehicle_id>/rent", views.rent, name="rent")
]