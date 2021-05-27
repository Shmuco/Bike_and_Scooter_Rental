from django.shortcuts import render, redirect
from django.urls import path, include
from .models import *
from .forms import *

# Create your views here.
def all_rentals(request):

    all_rentals = Rental.objects.all()
    print(all_rentals)
    return render(request, 'all_rentals.html', {'rentals': all_rentals})

def single_customer(request, customer_id):
    customer = Customer.objects.get(id=customer_id)
    print(customer.rentals())
    return render(request, 'single_customer.html', {'customer': customer})


def single_vehicle(request, vehicle_id):
    vehicle = Vehicle.objects.get(id=vehicle_id)
  
    return render(request, 'single_vehicle.html', {'vehicle': vehicle})

def add_vehicle(request):
    if request.method == 'GET':
        print(VehicleForm())
        return render(request, 'add_vehicle.html', {'form': VehicleForm(),'add_type': 'Vehicle'})

    if request.method == 'POST':
        data = request.POST
        form = VehicleForm(data)
        if form.is_valid():
            Vehicle.objects.create(**form.cleaned_data)
    return redirect('add_vehicle')


def add_customer(request):
    if request.method == 'GET':
            return render(request, 'add_customer.html', {'form': CustomerForm(),'add_type': 'Vehicle'})

    if request.method == 'POST':
        data = request.POST
        form = CustomerForm(data)
        if form.is_valid():
            Customer.objects.create(**form.cleaned_data)
    return redirect('add_customer')


def add_rental(request):
    if request.method == 'GET':
            return render(request, 'add_rental.html', {'form': RentalForm(),'add_type': 'Rental'})

    if request.method == 'POST':
        data = request.POST
        form = RentalForm(data)
        if form.is_valid():
            Rental.objects.create(**form.cleaned_data)
    return redirect('add_customer')

