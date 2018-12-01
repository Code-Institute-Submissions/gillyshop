from django.conf.urls import url, include
from .views import products, new, cactus, flamingos, palm, pink, deer, galaxy, product_detail, TagIndexView


urlpatterns = [
    url(r'^$', products, name="products"),
    url(r'^new/$', new, name="new"),
    url(r'^cactus/$', cactus, name="cactus"),
    url(r'^flamingos/$', flamingos, name="flamingos"),
    url(r'^palm/$', palm, name="palmtrees"),
    url(r'^pink/$', pink, name="pink"),
    url(r'^deer/$', deer, name="deer"),
    url(r'^galaxy/$', galaxy, name="galaxy"),
    url(r'^(?P<pk>\d+)/$', product_detail, name="product_detail"),
    url(r'^tag/(?P<slug>[-\w]+)/$', TagIndexView.as_view(), name='tagpage'),
    ]
    
    
