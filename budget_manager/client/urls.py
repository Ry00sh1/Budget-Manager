from django.urls import path
from .views import newClient, listClient

app_name = "client"
urlpatterns = [
    path("add/", newClient, name="add-client"),
    path("list/", listClient, name="list-client"),
]
