from django.urls import path
from storeApp.views import index, products, search, products_detail

urlpatterns = [
    path("", index, name="index"),
    path("urunler/", products, name="product"),
    path("urunler/<int:id>/<slug:slug>", products_detail, name="product_detail"),
    path("search/", search, name="search"),
]