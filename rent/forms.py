from django import forms 
from .models import *

class VehicleForm(forms.Form):
    vehicle_type = forms.ModelChoiceField(VehicleType.objects.all())
    real_cost = forms.FloatField()
    vehicle_size = forms.ModelChoiceField(VehicleSize.objects.all())

class CustomerForm(forms.Form):
    first_name = forms.CharField(max_length=200)
    last_name = forms.CharField(max_length=200)
    email = forms.EmailField()
    phone_number = forms.CharField(max_length=200)
    address = forms.CharField(max_length=200)
    city = forms.CharField(max_length=200)
    country  = forms.CharField(max_length=200)

class RentalForm(forms.Form):
    customer = forms.ModelChoiceField(Customer.objects.all())
    return_date = models.DateTimeField()
    vehicle = forms.ModelChoiceField(Vehicle.objects.all())

