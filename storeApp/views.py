from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from cart.cart import Cart
from storeApp.models import Categories, Product, Brand, Color, Filter_Price, Contact, CartOrder
import iyzipay
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
import json
import requests
from django.urls import reverse
from django.http import HttpResponseRedirect, HttpResponse


def get_settings(request):
    products = Product.objects.filter(status="Publish").order_by("-id")
    categories = Categories.objects.all()
    brands = Brand.objects.all()
    colors = Color.objects.all()
    prices = Filter_Price.objects.all()
    CATID = request.GET.get('categories')
    PRICE_FILTER_ID = request.GET.get('prices')
    COLOR_ID = request.GET.get('colors')
    BRANDS_ID = request.GET.get('brands')
    ATOZID = request.GET.get('ATOZ')
    ZTOAID = request.GET.get('ZTOA')
    PRICELOWTOHIGH = request.GET.get('PRICELOWTOHIGH')
    PRICEHOWTOLOW = request.GET.get('PRICEHOWTOLOW')
    NEWPRODUCT = request.GET.get('NEWPRODUCT')
    OLDPRODUCT = request.GET.get('OLDPRODUCT')
    
    if CATID:
        products = Product.objects.filter(categories__id = CATID, status="Publish").order_by("-id")
    elif PRICE_FILTER_ID:
        products = Product.objects.filter(filter_price__id = PRICE_FILTER_ID, status="Publish").order_by("-id")
    elif COLOR_ID:
        products = Product.objects.filter(color__id = COLOR_ID, status="Publish").order_by("-id")
    elif BRANDS_ID:
        products = Product.objects.filter(brand__id = BRANDS_ID, status='Publish').order_by("-id")
    elif ATOZID:
        products = Product.objects.filter(status = 'Publish').order_by('name')
    elif ZTOAID:
        products = Product.objects.filter(status = 'Publish').order_by('-name')
    elif PRICELOWTOHIGH:
        products = Product.objects.filter(status = 'Publish').order_by('price')
    elif PRICEHOWTOLOW:
        products = Product.objects.filter(status = 'Publish').order_by('-price')
    elif NEWPRODUCT:
        products = Product.objects.filter(status = 'Publish', condition = 'Yeni').order_by('-id')
    elif OLDPRODUCT:
        products = Product.objects.filter(status = 'Publish', condition = 'Eski').order_by('-id')
    else:
        products = Product.objects.filter(status="Publish").order_by("-id")
    
    context = {
        "products": products,
        'categories': categories,
        'brands': brands,
        'colors': colors,
        'prices': prices,
    }
    return context

def index(request):
    return render(request,"pages/index.html",get_settings(request))

def products(request):
    return render(request,"pages/products.html",get_settings(request))

def search(request):
    query = request.GET.get('query')
    products = Product.objects.filter(name__icontains=query)
    context = {
        "products": products,
    }
    return render(request,"partials/search.html",context)

def products_detail(request, id, slug):
    product = Product.objects.get(id=id, slug=slug)
    
    context = {
        "product": product,
    }
    
    return render(request,"pages/product_detail.html",context)

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        
        contact = Contact(
            name = name,
            email = email,
            subject = subject,
            message = message
        )
        
        subject = subject
        message = message 
        email_from = settings.EMAIL_HOST_USER
        try:
            send_mail(subject, message, email_from, ['dd7490623@gmail.com'])
            contact.save()
            return redirect('index')
        except:
            return redirect('contact')
        
    return render(request,"pages/contact.html")

def user_register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        pass1 = request.POST.get('pass1')
        pass2 = request.POST.get('pass2')
        
        customer = User.objects.create_user(username=username, first_name=first_name, last_name=last_name, email=email, password=pass1)
        
        customer.first_name = first_name
        customer.last_name = last_name
        
        customer.save()
        
        return redirect('user_login')
        
    return render(request,"pages/registiration/auth.html")

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            return redirect('user_login')
    
    return render(request,"pages/registiration/auth.html")

def user_logout(request):
    logout(request)
    return redirect('user_login')

def card_details(request):
    return render(request,"pages/card/card_details.html")

@login_required(login_url="/giris/")
def cart_add(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.add(product=product)
    return redirect("index")

@login_required(login_url="/giris/")
def item_clear(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.remove(product)
    return redirect("cart_detail")

@login_required(login_url="/giris/")
def item_increment(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.add(product=product)
    return redirect("cart_detail")

@login_required(login_url="/giris/")
def item_decrement(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.decrement(product=product)
    return redirect("cart_detail")

@login_required(login_url="/giris/")
def cart_clear(request):
    cart = Cart(request)
    cart.clear()
    return redirect("cart_detail")

@login_required(login_url="/giris/")
def cart_detail(request):
    return render(request, 'pages/card/card_details.html')

@login_required(login_url="/giris/")
def cart_checkout(request):
    return render(request, 'pages/card/checkout.html')

api_key = 'sandbox-pjriaDcg7LZeMhDtrGznoXDiJpKTPjwh'

secret_key = 'sandbox-W60SybR9duT1ceFVmzaKhGTITtcVv3yd'

base_url = 'sandbox-api.iyzipay.com'

options = {
    'api_key': api_key,
    'secret_key': secret_key,
    'base_url': base_url
}

dictToken = list()

def payment(request):
    context = dict()
    
    sepet = CartOrder.objects.all()
    odeme = list()
    
    for i in sepet:
        odeme.append(i.user)
        odeme.append(i.product)
        odeme.append(i.quantity * i.price)
        print("----------------", odeme)
        
    buyer = {
        'id': 'BY789',
        'name': 'John',
        'surname': 'Doe',
        'gsmNumber': '+905350000000',
        'email': 'email@email.com',
        'identityNumber': '74300864791',
        'lastLoginDate': '2015-10-05 12:43:35',
        'registrationDate': '2013-04-21 15:12:09',
        'registrationAddress': 'Nidakule Göztepe, Merdivenköy Mah. Bora Sok. No:1',
        'ip': '85.34.78.112',
        'city': 'Istanbul',
        'country': 'Turkey',
        'zipCode': '34732'
    }
    
    address = {
        'contactName': 'Jane Doe',
        'city': 'Istanbul',
        'country': 'Turkey',
        'address': 'Nidakule Göztepe, Merdivenköy Mah. Bora Sok. No:1',
        'zipCode': '34732'
    }
    
    basket_items = [
        {
            'id': 'BI101',
            'name': 'Binocular',
            'category1': 'Collectibles',
            'category2': 'Accessories',
            'itemType': 'PHYSICAL',
            'price': '0.3'
        },
        {
            'id': 'BI102',
            'name': 'Game code',
            'category1': 'Game',
            'category2': 'Online Game Items',
            'itemType': 'VIRTUAL',
            'price': '0.5'
        },
        {
            'id': 'BI103',
            'name': 'Usb',
            'category1': 'Electronics',
            'category2': 'Usb / Cable',
            'itemType': 'PHYSICAL',
            'price': '0.2'
        }
    ]
    
    request = {
        'locale': 'tr',
        'conversationId': '123456789',
        'price': '1',
        'paidPrice': '1.2',
        'currency': 'TRY',
        'basketId': 'B67832',
        'paymentGroup': 'PRODUCT',
        "callbackUrl": "http://localhost:8000/sepet/sepet-detay/odeme/result/",
        "enabledInstallments": ['2', '3', '6', '9'],
        'buyer': buyer,
        'shippingAddress': address,
        'billingAddress': address,
        'basketItems': basket_items,
        #'debitCardAllowed': True
    }
    
    checkout_form_initialize = iyzipay.CheckoutFormInitialize().create(request, options)
    
    page = checkout_form_initialize
    
    header = {'Content-Type': 'application/json'}
    
    content = checkout_form_initialize.read().decode('utf-8')
    
    json_content = json.loads(content)
    
    print("--------------------")
    print(json_content)
    print("--------------------")
    print("Gelen Veri tipi: ", type(json_content))
    print("--------------------")
    print(json_content['token'])
    
    if 'token' in json_content:
        dictToken.append(json_content['token'])
    else:
        # 'token' anahtarı yoksa veya içeriği beklenmedikse bir işlem yapabilirsiniz
        print("Hata: 'token' anahtarı bulunamadı veya beklenmeyen bir durum oluştu.")
    
    return HttpResponse(json_content["checkoutFormContent"])     


@require_http_methods(["GET","POST"])
@csrf_exempt
def result(request):
    context = dict()
    
    url = request.META.get('index')
    
    print('Result içinde ki token: ', dictToken)
    
    token = None
    
    if dictToken:
        token = dictToken[0]
    
    request = {
        'locale': 'tr',
        'conversationId': '123456789',
        'token': token
    }
    
    check_out_form = iyzipay.CheckoutForm().retrieve(request, options)
    
    print('-------------------')
    print(type(check_out_form))
    
    result = check_out_form.read().decode('utf-8')
    
    print('-------------------')
    print(token)
    print('-------------------')
    
    sonuc = json.loads(result, object_pairs_hook=list)
    
    print('-------------------')
    for i in sonuc:
        print(i)
    print('-------------------')
    
    if sonuc[0][1] == 'success':
        context['success'] = 'Başarılı işlemler'
        
        return HttpResponseRedirect(reverse('success'), context)
    
    elif sonuc[0][1] == 'failure':
        context['failure'] = 'Başarısız işlemler'
        
        return HttpResponseRedirect(reverse('failure'), context)
    
    return HttpResponseRedirect(reverse(url), context)

def success(request):
    context = dict()
    
    context['success'] = 'İşlem başarılı'
    
    template = 'pages/payment/ok.html'
    
    return render(request, template, context)

def failure(request):
    context = dict()
    
    context['failure'] = 'İşlem başarısız'
    
    template = 'pages/payment/fail.html'
    
    return render(request, template, context)

