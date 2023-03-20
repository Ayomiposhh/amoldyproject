from decimal import Decimal
from django.conf import settings
from amoldy_app.models import Shop


class Basket():
    """
    A base Basket class, providing some default behaviors that
    can be inherited or overrided, as necessary.
    """

    def __init__(self, request):
        self.session = request.session
        basket = self.session.get(settings.BASKET_SESSION_ID)
        if settings.BASKET_SESSION_ID not in request.session:
            basket = self.session[settings.BASKET_SESSION_ID] = {}
        self.basket = basket

    def add(self, shop, qty):
        """
        Adding and updating the users basket session data
        """
        shop_id = str(shop.id)

        if shop_id in self.basket:
            self.basket[shop_id]['qty'] = qty
        else:
            self.basket[shop_id] = {'price': str(shop.price), 'qty': qty}

        self.save()

    def __iter__(self):
        """
        Collect the product_id in the session data to query the database
        and return products
        """
        shop_ids = self.basket.keys()
        shop = Shop.shop.filter(id__in=shop_ids)
        basket = self.basket.copy()

        for shop in Shop:
            basket[str(shop.id)]['shop'] = shop

        for item in basket.values():
            item['price'] = Decimal(item['price'])
            item['total_price'] = item['price'] * item['qty']
            yield item

    def __len__(self):
        """
        Get the basket data and count the qty of items
        """
        return sum(item['qty'] for item in self.basket.values())

    def update(self, shop, qty):
        """
        Update values in session data
        """
        shop_id = str(shop)
        if shop_id in self.basket:
            self.basket[shop_id]['qty'] = qty
        self.save()

    def get_subtotal_price(self):
        return sum(Decimal(item['price']) * item['qty'] for item in self.basket.values())

    def get_total_price(self):

        subtotal = sum(Decimal(item['price']) * item['qty'] for item in self.basket.values())

        if subtotal == 0:
            shipping = Decimal(0.00)
        else:
            shipping = Decimal(11.50)

        total = subtotal + Decimal(shipping)
        return total

    def delete(self, shop):
        """
        Delete item from session data
        """
        shop_id = str(shop)

        if shop_id in self.basket:
            del self.basket[shop_id]
            self.save()

    def clear(self):
        # Remove basket from session
        del self.session[settings.BASKET_SESSION_ID]
        self.save()

    def save(self):
        self.session.modified = True
