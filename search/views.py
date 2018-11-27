from django.shortcuts import render
from products.models import Product
from django.core.exceptions import ObjectDoesNotExist

# Create your views here.


def do_search(request):
    # products = Product.objects.filter(name__icontains=request.GET['q'])
    products = Product.objects.filter(name__icontains=request.GET['q']) | Product.objects.filter(description__icontains=request.GET['q'])
    return render(request, "products.html", {"products":products})
    else ObjectDoesNotExist:
        print("Either the entry or blog doesn't exist.")
    
    
