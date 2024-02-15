from django.shortcuts import render
from storeApp.models import Categories, Product, Brand, Color, Filter_Price

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