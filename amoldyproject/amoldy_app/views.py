from django.shortcuts import render
from amoldy_app.forms import *
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView

# Create your views here.

def home(request):
  return render(request,'amoldy_app/index.html')

class Product_Shop(ListView):
    model = Shop
    template_name = 'amoldy_app/shop.html'
    context_object_name = 'sp'
    paginate_by = 1
    # search = SearchForm()
    

    def get_queryset(self):
        return Shop.objects.order_by('-created')
    
    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        
        return context





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


def detail(request, slug):
  post = get_object_or_404(Shop, slug=slug, in_stock=True)
  return render(request,'amoldy_app/detail.html',{'product':post,})
  
   
 


