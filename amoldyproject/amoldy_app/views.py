from django.shortcuts import render
from amoldy_app.forms import *
from django.shortcuts import render, get_object_or_404

# Create your views here.

def home(request):
  return render(request,'amoldy_app/index.html')

def shop(request):
  sp = Shop.objects.all()[:9]
  return render(request,'amoldy_app/shop.html',{'sp' : sp,})

def cart(request):
  return render(request,'amoldy_app/cart.html')

def checkout(request):
  return render(request,'amoldy_app/checkout.html')

def contact(request):
  if request.method =='POST':
    contact_form = ContactForm(request.POST)
    if contact_form.is_valid():
      contact_form.save() 
  else:
    contact_form = ContactForm()  
  return render(request,'amoldy_app/contact.html',{'cform':contact_form})



def detail(request,post_id):
  template_name= 'amoldy_app/detail.html'
  post = get_object_or_404(Shop, id=post_id)
  

  return render(request,'amoldy_app/detail.html',{'shop_detail':post,})


