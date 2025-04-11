from django.contrib import admin
from django.urls import path
from .views import newBudget

urlpatterns = [
    path("new-budget/", newBudget, name="new-budget"),
]