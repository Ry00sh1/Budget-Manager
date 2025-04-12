from django.urls import path
from .views import newClient, listClient

urlpatterns = [
    path("add-client/", newClient, name="add-client"),
    path("list-client/", listClient, name="list-client"),
]
