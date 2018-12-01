from django.shortcuts import render
from products.models import Product
from django.core.exceptions import ObjectDoesNotExist
from django.contrib import messages

# Code adapted from lessons/added to by me


# def do_search(request):
#     products = Product.objects.filter(name__icontains=request.GET['q']) | Product.objects.filter(description__icontains=request.GET['q'])
#     return render(request, "products.html", {"products":products})



# def do_search(request):
#     products = Product.objects.filter(name__icontains=request.GET['q']) | Product.objects.filter(description__icontains=request.GET['q'])
#     for product in products:
#         if product:
#             return render(request, "products.html", {"products":products})
#         else:
#             messages.error(request, "We were unable to take a payment with that card")
#             return render(request, "products.html", {"products":products})

def do_search(request):
    products = Product.objects.filter(name__icontains=request.GET['q']) | Product.objects.filter(description__icontains=request.GET['q'])
    if products:
        return render(request, "products.html", {"products":products})
    else:
        messages.error(request, "We were unable to take a payment with that card")
        return render(request, "products.html", {})


