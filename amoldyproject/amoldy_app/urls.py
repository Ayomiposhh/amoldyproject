from django.urls import path, include 
from amoldy_app import views
from django.contrib.auth import views as auth_views



app_name='amoldy_app'


urlpatterns = [
  path('home/', views.home, name='home'),
  path('shop/',  views.Product_Shop.as_view(), name='shop'),
  path('cart/', views.cart, name='cart'),
  path('checkout/', views.checkout, name='checkout'),
  path('contact/', views.contact, name='contact'),
  path('detail/<slug:slug>', views.detail, name='shop_detail'),
  
  
  
  
]