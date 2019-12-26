from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('search',views.search),
    path('price_filter',views.price_filter),
    path('about',views.about),
    path('contact',views.contact),
]
