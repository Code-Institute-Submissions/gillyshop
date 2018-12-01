from django.shortcuts import render, get_object_or_404, redirect, render_to_response
from django.views.generic import ListView
from .models import Product
from taggit.models import Tag
# Create your views here.


#view written by me/adapted from lessons
def products(request):
    products = Product.objects.all()
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


# View written by me with help from my mentor, solution found here https://godjango.com/33-tagging-with-django-taggit/
class TagIndexView(ListView):
    template_name = 'tagpage.html'
    model = Product
    paginate_by = '10'

   
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['products'] = Product.objects.filter(tags__slug=self.kwargs.get('slug'))
        context['tagname'] = self.kwargs.get('slug')
        return context 

    
