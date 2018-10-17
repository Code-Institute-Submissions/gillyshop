from django.shortcuts import render, get_object_or_404, redirect
from .models import Product, Image

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
    return render(request, "flamingos.html", {"products": flamingoproducts})
    
def palm(request):
    palmproducts = Product.objects.filter(category="Palm")
    return render(request, "palmtrees.html", {"products": palmproducts})
    
def pink(request):
    pinkproducts = Product.objects.filter(category="Pink")
    return render(request, "pink.html", {"products": pinkproducts})
    
def deer(request):
    deerproducts = Product.objects.filter(category="Deer")
    return render(request, "deer.html", {"products": deerproducts})
    
def galaxy(request):
    galaxyproducts = Product.objects.filter(category="Galaxy")
    return render(request, "galaxies.html", {"products": galaxyproducts})


def product_detail(request, pk):
    productdetail = get_object_or_404(Product, pk=pk)
    return render(request, "product_detail.html", {"products":productdetail})
 
    

       


    

# def product_page(request, slug):
#     products = get_object_or_404(Product, slug=slug)
#     # products = Product.objects.self
#     return render(request, "products/product_page.html", {"products":products})