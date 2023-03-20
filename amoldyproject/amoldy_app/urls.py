from django.urls import path, include 
from amoldy_app import views
from django.contrib.auth import views as auth_views



app_name='amoldy_app'


urlpatterns = [
  path('home/', views.home, name='home'),
  path('shop/', views.shop, name='shop'),
  path('cart/', views.cart, name='cart'),
  path('checkout/', views.checkout, name='checkout'),
  path('contact/', views.contact, name='contact'),
  path('detail/<int:post_id>', views.detail, name='shop_detail'),
  
  
  
  
]