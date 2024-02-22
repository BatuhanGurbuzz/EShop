from django.db import models
from django.utils.text import slugify
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User
class Categories(models.Model):
    name = models.CharField(max_length = 200, verbose_name = "Kategori Adı")
    
    slug = models.SlugField(default = "",blank=True,null = False, unique=True, db_index=True)
    
    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        return super().save(*args, **kwargs)
    
    class Meta:
        verbose_name = "Kategori"
        verbose_name_plural = "Kategoriler"
class Brand(models.Model):
    name = models.CharField(max_length = 200, verbose_name = "Marka Adı")
    description = models.TextField(verbose_name = "Açıklama", blank = True, null = True)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Marka"
        verbose_name_plural = "Markalar"

class Color(models.Model):
    name = models.CharField(max_length = 200, verbose_name = "Renk Adı")
    code = models.CharField(max_length = 50, verbose_name = "Renk Kodu")
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Renk"
        verbose_name_plural = "Renkler"
    
    
class Filter_Price(models.Model):
    FILTER_PRICE = (
        ('0- 1000', '1000-2000'),
        ('2000-3000', '3000-4000'),
        ('4000-5000', '5000-6000'),
        ('6000-7000', '7000-8000'),
        ('8000-9000', '9000-10000'),
        ('10000 - ∞' , '∞ - ∞')
    )
    price = models.CharField(choices = FILTER_PRICE, max_length = 60, verbose_name = "Fiyat Aralığı")
    
    description = models.TextField(verbose_name = "Açıklama", blank = True, null = True)
    
    def __str__(self):
        return self.price
    
    class Meta:
        verbose_name = "Fiyat aralığı"
        verbose_name_plural = "Fiyatlar"
        
class Product(models.Model):
    STOCK = (
        ('AVAILABLE', 'Mevcut'),
        ('NOT AVAILABLE', 'Mevcut Değil'),
    )
    
    STATUS = (
        ('Publish', 'Aktif'), 
        ('Draft', 'Pasif')
    )
    
    CONDITION = (
        ('New', 'Yeni'),
        ('OLD', 'Eski')
    )
    
    unique_id = models.CharField(unique = True, max_length = 200, verbose_name = "Ürün Kodu", null=True, blank=True)
    
    image = models.ImageField(upload_to = 'products/', verbose_name = "Ürün Resmi")
    
    name = models.CharField(max_length = 200, verbose_name = "Ürün Adı")
    
    price = models.IntegerField(verbose_name = "Fiyat")
    
    information = RichTextField(verbose_name = "Ürün Bilgisi", null=True, blank=True)
    
    description = RichTextField(verbose_name = "Ürün Açıklaması", null=True, blank=True)
    
    stock = models.CharField(choices = STOCK, max_length = 60, verbose_name = "Stok Durumu")
    
    status = models.CharField(choices = STATUS, default = "Publish",max_length = 200, verbose_name = "Durum")
    
    condition = models.CharField(choices = CONDITION, default='Yeni', max_length = 200, verbose_name = "Ürün Durumu")
    
    created_date = models.DateTimeField(auto_now_add = True, verbose_name = "Oluşturulma Tarihi")
    
    updated_date = models.DateTimeField(auto_now = True, verbose_name = "Güncellenme Tarihi")
    
    categories = models.ForeignKey(Categories, on_delete = models.CASCADE, verbose_name = "Kategori")
    
    brand = models.ForeignKey(Brand, on_delete = models.CASCADE, verbose_name = "Marka")
    
    color = models.ForeignKey(Color, on_delete = models.DO_NOTHING, verbose_name = "Renk")
    
    filter_price = models.ForeignKey(Filter_Price, on_delete = models.CASCADE, verbose_name = "Fiyat Aralığı")
    
    slug = models.SlugField(default = "",blank=True,null = False, unique=True, db_index=True, verbose_name = "Slug")
    
    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        
        if self.unique_id is None and self.created_date and self.id:
            self.unique_id = self.created_date.strftime('75%Y%m%d23') + str(self.pk)
            
        return super().save(*args, **kwargs)
            
        
        
    class Meta:
        verbose_name = "Ürün"
        verbose_name_plural = "Ürünler"
    

class Images(models.Model):
    image = models.ImageField(upload_to = 'products/', verbose_name = "Ürün Resmi")
    
    product = models.ForeignKey(Product, on_delete = models.CASCADE, verbose_name = "Ürün")
    
    def __str__(self):
        return self.image.url
    
    class Meta:
        verbose_name = "Resim"
        verbose_name_plural = "Resimler"
    
class Tag(models.Model):   
    name = models.CharField(max_length = 200, verbose_name = "Etiket Adı")
    
    product = models.ForeignKey(Product, on_delete = models.CASCADE, verbose_name = "Ürün")
    
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = "Etiket"
        verbose_name_plural = "Etiketler"
        
class Contact(models.Model):
    name = models.CharField(max_length = 200, verbose_name = "İsim")
    
    email = models.EmailField(max_length = 200, verbose_name = "E-Posta")
    
    subject = models.CharField(max_length = 200, verbose_name = "Konu")
    
    message = models.TextField(verbose_name = "Mesaj")
    
    date = models.DateTimeField(auto_now_add = True, verbose_name = "Tarih")
    
    def __str__(self):
        return self.email
    
    class Meta:
        verbose_name = "İletişim"
        verbose_name_plural = "İletişimler"
        
class Order(models.Model):
    PAID = (
        ('Paid', 'Ödendi'),
        ('Not Paid', 'Ödenmedi'),
    )
    
    user = models.ForeignKey(User, on_delete = models.CASCADE, verbose_name = "Kullanıcı")
    
    firstname = models.CharField(max_length = 200, verbose_name = "Ad")
    
    lastname = models.CharField(max_length = 200, verbose_name = "Soyad")
    
    country = models.CharField(max_length = 200, verbose_name = "Ülke")
    
    address = models.TextField(verbose_name = "Adres")
    
    city = models.CharField(max_length = 200, verbose_name = "Şehir")
    
    state = models.CharField(max_length = 200, verbose_name = "İlçe")
    
    postcode = models.IntegerField(verbose_name = "Posta Kodu")
    
    phone = models.IntegerField(verbose_name = "Telefon")
    
    email = models.EmailField(max_length = 200, verbose_name = "E-Posta")
    
    additional_information = models.TextField(verbose_name = "Ek Bilgi", blank = True, null = True)
    
    amount = models.IntegerField(verbose_name = "Tutar")
    
    payment_id = models.CharField(max_length = 200, null = True, blank = True, verbose_name = "Ödeme ID")
    
    paid = models.CharField(choices = PAID, default = "Ödenmedi", max_length = 200, verbose_name = "Ödeme Durumu")
    
    date = models.DateTimeField(auto_now_add = True, verbose_name = "Tarih")
    
    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name = "Sipariş"
        verbose_name_plural = "Siparişler"
        
class CartOrder(models.Model):
    STATUS = (
        ('New', 'Sipariş Alındı'),
        ('Accepted', 'Hazırlanıyor'),
        ('Cancelled', 'İptal Edildi'),
        ('Completed', 'Tamamlandı'),
        ('Returned', 'İade Edildi'),
        ('Shipped', 'Kargoya Verildi'),
    )
    
    order = models.ForeignKey(Order, on_delete = models.CASCADE, verbose_name = "Sipariş")
    
    product = models.ForeignKey(Product, on_delete = models.CASCADE, verbose_name = "Ürün")
    
    image = models.ImageField(upload_to = 'products/', verbose_name = "Ürün Resmi")
    
    quantity = models.CharField(max_length = 200, verbose_name = "Miktar")
    
    price = models.CharField(max_length = 200, verbose_name = "Fiyat")
    
    total = models.CharField(max_length = 200, verbose_name = "Toplam")
    
    status = models.CharField(choices = STATUS, default = "New", max_length = 200, verbose_name = "Durum")
    
    def __str__(self):
        return self.order.user.username
    
    class Meta:
        verbose_name = "Sipariş Ürün"
        verbose_name_plural = "Sipariş Ürünler"
    