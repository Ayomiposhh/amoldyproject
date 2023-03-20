from django.shortcuts import render
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render

from amoldy_app.models import Shop

from .basket import Basket


def basket_summary(request):
    basket = Basket(request)
    return render(request, 'basket/summary.html', {'basket': basket})


def basket_add(request):
    basket = Basket(request)
    if request.POST.get('action') == 'post':
        shop_id = int(request.POST.get('shopid'))
        shop_qty = int(request.POST.get('shopqty'))
        shop = get_object_or_404(Shop, id=shop_id)
        basket.add(product=shop, qty=shop_qty)

        basketqty = basket.__len__()
        response = JsonResponse({'qty': basketqty})
        return response


def basket_delete(request):
    basket = Basket(request)
    if request.POST.get('action') == 'post':
        shop_id = int(request.POST.get('shopid'))
        basket.delete(product=shop_id)

        basketqty = basket.__len__()
        baskettotal = basket.get_total_price()
        response = JsonResponse({'qty': basketqty, 'subtotal': baskettotal})
        return response


def basket_update(request):
    basket = Basket(request)
    if request.POST.get('action') == 'post':
        shop_id = int(request.POST.get('shopid'))
        shop_qty = int(request.POST.get('shopqty'))
        basket.update(product=shop_id, qty=shop_qty)

        basketqty = basket.__len__()
        baskettotal = basket.get_total_price()
        response = JsonResponse({'qty': basketqty, 'subtotal': baskettotal})
        return response

# Create your views here.
