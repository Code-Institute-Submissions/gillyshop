from django.contrib import admin
from products.models import Product, Picture

# Register your models here.
class PictureInline(admin.TabularInline):
    model = Picture
    fields = ['picture',]
    
class ProductAdmin(admin.ModelAdmin):
    inlines = [PictureInline,]
    
admin.site.register(Product, ProductAdmin)