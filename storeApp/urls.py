from django.urls import path
from storeApp.views import index, products, search, products_detail, contact, user_login, user_register, user_logout, cart_detail, cart_add, item_clear, item_increment, item_decrement, cart_clear, cart_checkout, payment, success, failure, result

urlpatterns = [
    path("", index, name="index"),
    path("urunler/", products, name="product"),
    path("urunler/<int:id>/<slug:slug>", products_detail, name="product_detail"),
    path("search/", search, name="search"),
    path("iletisim/", contact, name="contact"),
    path("kayit/", user_register, name="user_register"),
    path('giris/', user_login, name='user_login'),
    path('cikis/', user_logout, name='user_logout'),
    # Sepet
    path("sepet/", cart_detail, name="card_details"),
    path("sepet/sepete-ekle/<int:id>/", cart_add, name='cart_add'),
    path("sepet/sepetten-çıkar/<int:id>/", item_clear, name='item_clear'),
    path("sepet/sepet-adet-arttır/<int:id>/", item_increment, name='item_increment'),
    path("sepet/sepet-adet-azalt/<int:id>/", item_decrement, name='item_decrement'),
    path("sepet/sepeti-temizle/", cart_clear, name='cart_clear'),
    path("sepet/sepet-detay/", cart_detail,name='cart_detail'),
    path("sepet/sepet-detay/sepet-kontrol/", cart_checkout, name='cart_checkout'),
    path('sepet/sepet-detay/odeme/', payment, name='payment'),
    path('sepet/sepet-detay/odeme/success/', success, name='success'),
    path('sepet/sepet-detay/odeme/failure/', failure, name='failure'),
    path('sepet/sepet-detay/odeme/result/', result, name='result'),
]