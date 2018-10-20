from django.conf.urls import url, include
from .views import all_products, new, cactus, flamingos, palm, pink, deer, galaxy, product_detail


urlpatterns = [
    url(r'^$', all_products, name="products"),
    url(r'^new/$', new, name="new"),
    url(r'^cactus/$', cactus, name="cactus"),
    url(r'^flamingos/$', flamingos, name="flamingos"),
    url(r'^palm/$', palm, name="palmtrees"),
    url(r'^pink/$', pink, name="pink"),
    url(r'^deer/$', deer, name="deer"),
    url(r'^galaxy/$', galaxy, name="galaxy"),
    url(r'^(?P<pk>\d+)/$', product_detail, name="product_detail"),
    ]
    
    
    
    
    
    # url(r'^product_page/$', product_page, name="product_page"),
    # found here https://blog.muva.tech/lesson-4-defining-url-patterns-template-shop-products-django-2-0-python-3-6/
    # url(r'^(?P<id>\d+)/(?P<slug>[-\w]+)/$', product_page, name="product_page"),
    # url('^(?P<slug>[^/]+)/$', "product_page"),
  
    
    
#     # found here https://django-fluent-pages.readthedocs.io/en/latest/newpagetypes/urls.html
# class ProductPage:
    
#     url('products.views', url('^(?P<slug>[^/]+)/$', 'product_page'),)
