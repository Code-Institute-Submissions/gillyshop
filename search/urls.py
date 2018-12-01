from django.conf.urls import url
from .views import do_search

# Code adapted/taken from lessons

urlpatterns= [
    url(r'^$', do_search, name='search'),
    ]