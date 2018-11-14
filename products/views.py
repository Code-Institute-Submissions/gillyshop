from django.shortcuts import render, get_object_or_404, redirect, render_to_response
from django.views.generic import ListView
from .models import Product
from taggit.models import Tag
# Create your views here.

def products(request):
    products = Product.objects.all()
    return render(request, "products.html", {"products": products})
    # tags = Product.objects.filter(tags='slug')
    # tags = self.kwargs.get('slug')
    # if tag_slug:
    #     tag = get_object_or_404(Tag, slug=tag_slug)
    #     products = products(tags__in=[tag])
    

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['tagname'] = self.kwargs.get('slug')
    #     return context 
        
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
    
class TagMixin(object):
    def get_context_data(self, kwargs):
        context = super(TagMixin, self).get_context_data(kwargs)
        context['tags'] = Tag.objects.all()
        return context    
 
class TagIndexView(Tag Mixin, ListView):
    template_name = 'tagpage.html'
    model = Product
    paginate_by = '10'
    context_object_name = 'products'
    
    def get_queryset(self):
        return Product.objects.filter(tags__slug=self.kwargs.get('slug'))
   
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['products'] = Product.objects.filter(tags__slug=self.kwargs.get('slug'))
    #     context['tagname'] = self.kwargs.get('slug')
    #     return context 
        
# //solution found on youtube//        
# def tagpage(request, tag):
#     products = Product.objects.filter(tags__name=tag)
#     return render_to_response("tagpage.html", {"products":products, "tag":tag})

        
# def tag(request, tag):
#     products = Product.objects.filter(tag__name=tag)
#     return render(request, "tag.html", {"products":products, "tag":tag})
    
    
# def tag(request):
#     tags = Product.objects.filter(tags="blue")
#     return render(request, "tag.html", {"products":tags})

    # def get_queryset(self):
    #     return Product.objects.filter(tags__slug=self.kwargs.get('slug'))

   

# def tag(request, slug):
#     tag = get_object_or_404(Product, slug=slug)
#     return render(request, "tag.html", {"tag":tag})       


    

# def product_page(request, slug):
#     products = get_object_or_404(Product, slug=slug)
#     # products = Product.objects.self
#     return render(request, "products/product_page.html", {"products":products})