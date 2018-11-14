from django.conf.urls import url
from .views import checkout, paid


urlpatterns = [
    url(r'^$', checkout, name='checkout'),
    url(r'^$', paid, name='paid')
    ]