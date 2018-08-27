from django.contrib import admin
from products.models import Product, PostPicture

# Register your models here.
class PostPictureInline(admin.TabularInline):
    model = PostPicture
    fields = ['picture',]
    
class ProductAdmin(admin.ModelAdmin):
    inlines = [PostPictureInline,]
    
admin.site.register(Product, ProductAdmin)