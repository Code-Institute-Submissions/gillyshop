from django.conf.urls import url, include
from .views import all_products, new

urlpatterns = [
    url(r'^$', all_products, name="products"),
    url(r'^new/$', new, name="new"),
    ]