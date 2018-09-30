from django.shortcuts import render
from .models import Product

# Create your views here.

def all_products(request):
    products = Product.objects.all()
    return render(request, "products.html", {"products": products})

def new(request):
    return render(request, 'new.html')
    
def cactus(request):
    cactusproducts = Product.objects.filter(category="Cactus")
    return render(request, "cactus.html", {"products": cactusproducts})
    
def animals(request):
    animalproducts = Product.objects.filter(category="Animal")
    return render(request, "animals.html", {"products": animalproducts})
    
def flamingos(request):
    flamingoproducts = Product.objects.filter(category="Flamingo")
    return render(request, "flamingo.html", {"products": flamingoproducts})
    
def unicorns(request):
    unicornproducts = Product.objects.filter(category="Unicorns")
    return render(request, "unicorns.html", {"products": unicornproducts})