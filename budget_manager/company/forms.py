from django import forms
from .models import Budget

class BudgetForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ('title', 'description')