from django.contrib import admin
from .models import Product


# class ProdModelAdmin(admin.ModelAdmin):
#     list_display = ['tag_list']
    
#     def get_queryset(self, request):
#         return super(ProdModelAdmin, self).get_queryset(request).prefetch_related('tags')
        
#     def tag_list(self, obj):
#         return u", ".join(o.name for o in obj.tags.all())
        


# Register your models here.
admin.site.register(Product)
