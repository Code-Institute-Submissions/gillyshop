from django.conf.urls import url, include
from home.views import index

# define url for homepage

urlpatterns = [
    url(r'^$', index, name="index"),
    ]