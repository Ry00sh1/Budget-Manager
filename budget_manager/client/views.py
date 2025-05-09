from django.shortcuts import render, redirect
from django.http import request, HttpResponse,JsonResponse
from django.urls import reverse
from django.views.generic import CreateView
from .models import Client
from .forms import AddressForm, IndividualClientForm,CorporateClientForm
from django.template.loader import render_to_string


def newClient(request):
    form_choice = request.GET.get('type') or request.POST.get('type')
    client_form = None

    if form_choice == 'individual':
        if request.method == 'POST':
            client_form = IndividualClientForm(request.POST)
            address_form = AddressForm(request.POST)
            if client_form.is_valid() and address_form.is_valid():
                client = client_form.save(commit=False)
                address = address_form.save()
                client.address = address
                client.save()
                return redirect(reverse('client:list-client'))
        else:
            client_form = IndividualClientForm()
    
    elif form_choice == 'coorporate':
        if request.method == 'POST':
            client_form = CorporateClientForm(request.POST)
            address_form = AddressForm(request.POST)
            if client_form.is_valid() and address_form.is_valid():
                client = client_form.save(commit=False)
                address = address_form.save()
                client.address = address
                client.save()
                return redirect(reverse('client:list-client'))
        else:
            client_form = CorporateClientForm()
    address_form = AddressForm()

    return render(request, 'client/add_client.html', {
        'client_form': client_form,
        'address_form': address_form,
        'form_choice': form_choice,
    })

def listClient(request):
    clients = Client.objects.all()
    return render(request, 'client/list_client.html', {'clients':clients})