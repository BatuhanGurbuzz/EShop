from django.urls import path
from storeApp.views import index

urlpatterns = [
    path("", index, name="index"),
]