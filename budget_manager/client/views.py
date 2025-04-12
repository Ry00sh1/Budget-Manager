from django.shortcuts import render, redirect
from django.http import request, HttpResponse
from django.views.generic import CreateView
from .models import Client
from .forms import ClientForm, AddressForm

def home(request):
    HttpResponse(request,"Home")

def newClient(request):
    if request.method == 'POST':
        address_form = AddressForm(request.POST)
        client_form = clientForm(request.POST)

        if address_form.is_valid and client_form.is_valid():
            client_address = address_form.save()  # salva primeiro o endereço
            client = client_form.save(commit=False)
            client.address = client_address
            client.save()
            return redirect('/')
    else:
        address_form = AddressForm()
        client_form = clientForm()
    
    return render(request, 'client/add_client.html', {
        'address_form': address_form,
        'client_form': client_form,
    })

def listClient(request):
    companies = client.objects.all()
    return render(request, 'client/list_client.html', {'companies':companies})