from django.shortcuts import render
from django.http import request
from .forms import BudgetForm, ItemSaleForm, ServiceForm

def newBudget(request):

    if request.method == "POST":
        budget_form = BudgetForm(request.POST)
        item_sale_form = ItemSaleForm(request.POST)
        service_form = ServiceForm(request.POST)

        if budget_form.is_valid() and item_sale_form.is_valid() and service_form.is_valid():
            budget_service = item_sale_form.save()
            budget_item = service_form.save()
            budget = budget_form.save(commit=False)
            
            budget.service = budget_service
            budget.item_sale = budget_item
            budget.save()
            return redirect('/')

    else:
        budget_form = BudgetForm()
        item_sale_form = ItemSaleForm()
        service_form = ServiceForm()
    
    return render(request, 'budget/newbudget.html', {
        'budget_form': budget_form,
        'item_sale_form': item_sale_form,
        'service_form': service_form,
    })

