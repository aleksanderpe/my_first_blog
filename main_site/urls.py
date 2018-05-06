from django.urls import path
from . import views
from django.conf.urls import url


urlpatterns = [
    url(r'^$', views.index),
    url(r'^(?P<post_id>[0-9]+)$', views.details),
    url(r'^(?P<post_category>[a-zA-Z]+)$', views.category_view), #my first regex url!
]