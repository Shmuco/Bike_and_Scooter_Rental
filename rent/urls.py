from django.urls import path
from . import views

urlpatterns = [
    path('rent/rental', views.all_rentals, name = 'rental'),
    path('rent/customer/<int:customer_id>', views.single_customer, name ="single_customer"),
    path('rent/vehicle/<int:vehicle_id>', views.single_vehicle, name ="single_vehicle"),
    path('rent/vehicle/add', views.add_vehicle, name ="add_vehicle"),
    path('rent/customer/add', views.add_customer, name ="add_customer"),
    path('rent/rental/add', views.add_rental, name ="add_rental"),
]

