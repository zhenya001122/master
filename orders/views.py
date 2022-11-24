from django.shortcuts import render
from products.models import Purchase
from users.models import User
from orders.forms import OrderCreateForm, AddressCreateForm
from basket.basket import Basket


def order_create(request):
    basket = Basket(request)
    if request.method == 'POST':
        form_address = AddressCreateForm(request.POST)
        if form_address.is_valid():
            address = form_address.save(commit=False)
            address.user = request.user
            address.save()
            form = OrderCreateForm()
            order = form.save(commit=False)
            order.user = request.user
            order.address = address
            order.status = 'оплачен'
            order.save()
            for item in basket:
                Purchase.objects.create(order=order,
                                        user=request.user,
                                        product=item['product'],
                                        cost=item['cost'],
                                        quantity=item['quantity'])
            # очистка корзины
            basket.clear()
            return render(request, 'orders/created.html',
                          {'order': order})
    else:
        form_address = AddressCreateForm
    return render(request, 'orders/create.html',
                  {'basket': basket, "form_address": form_address})
