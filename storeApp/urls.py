from django.urls import path
from storeApp.views import index, products

urlpatterns = [
    path("", index, name="index"),
    path("urunler/", products, name="product")
]