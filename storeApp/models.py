from django.db import models
from django.utils.text import slugify
from ckeditor.fields import RichTextField
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
        
        