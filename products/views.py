from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView
from .models import Product
from taggit.models import Tag
# Create your views here.

def products(request):
    products = Product.objects.all()
    # if tag_slug:
    #     tag = get_object_or_404(Tag, slug=tag_slug)
    #     products = products(tags__in=[tag])
    return render(request, "products.html", {"products": products})

def new(request):
    return render(request, 'new.html')
    
def cactus(request):
    cactusproducts = Product.objects.filter(category="Cactus")
    return render(request, "cactus.html", {"products": cactusproducts})
    
    
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
    product = get_object_or_404(Product, pk=pk)
    return render(request, "product_detail.html", {"product": product})
 
class TagIndexView(ListView):
    # template_name = 'product_detail.html'
    model = Product
    paginate_by = '10'
    context_object_name = 'products'
    
    def get_queryset(self):
        return Product.objects.filter(tags__slug=self.kwargs.get('slug'))

# def tag(request, slug):
#     tag = get_object_or_404(Product, slug=slug)
#     return render(request, "tag.html", {"tag":tag})

def tag(request):
    return render(request, 'tag.html')
       


    

# def product_page(request, slug):
#     products = get_object_or_404(Product, slug=slug)
#     # products = Product.objects.self
#     return render(request, "products/product_page.html", {"products":products})