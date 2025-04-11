from django.shortcuts import render, redirect
from django.http import request, HttpResponse
from django.views.generic import CreateView
from .models import Company
from .forms import CompanyForm, AddressForm

def home(request):
    HttpResponse(request,"Home")

def newCompany(request):
    if request.method == 'POST':
        address_form = AddressForm(request.POST)
        company_form = CompanyForm(request.POST)

        if address_form.is_valid and company_form.is_valid():
            company_address = address_form.save()  # salva primeiro o endereço
            company = company_form.save(commit=False)
            company.address = company_address
            company.save()
            return redirect('/')
    else:
        address_form = AddressForm()
        company_form = CompanyForm()
    
    return render(request, 'company/addcompany.html', {
        'address_form': address_form,
        'company_form': company_form,
    })

def listCompany(request):
    companies = Company.objects.all()
    return render(request, 'company/listcompany.html', {'companies':companies})