from django.conf.urls import url, include
from .views import all_products, new, cactus

urlpatterns = [
    url(r'^$', all_products, name="products"),
    url(r'^new/$', new, name="new"),
    url(r'^cactus/$', cactus, name="cactus"),
    ]