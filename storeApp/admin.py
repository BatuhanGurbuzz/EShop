from django.contrib import admin
from storeApp.models import Categories, Brand, Color, Filter_Price, Product, Images, Tag


@admin.register(Categories)
class CategoriesAdmin(admin.ModelAdmin):
    list_display = ['slug', 'name',]
    list_editable = ['name',]
    search_fields = ['name',]
    
@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ['description','name',]
    list_editable = ['name',]
    search_fields = ['name',]
    
@admin.register(Color)
class ColorAdmin(admin.ModelAdmin):
    list_display = ['code','name',]
    search_fields = ['name', 'code']
    
@admin.register(Filter_Price)
class Filter_PriceAdmin(admin.ModelAdmin):
    list_display = ['description','price',]
    list_editable = ['price',]


class ImagesInline(admin.TabularInline):
    model = Images

class TagInline(admin.TabularInline):
    model = Tag
    
class ProductAdmin(admin.ModelAdmin):
    inlines = [ImagesInline, TagInline]
    

admin.site.register(Product, ProductAdmin)
    


    
