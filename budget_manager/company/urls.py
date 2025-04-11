from django.urls import path
from .views import newCompany, listCompany

urlpatterns = [
    path("add-company/", newCompany, name="add-company"),
    path("list-company/", listCompany, name="list-company"),
]
