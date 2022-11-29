from django.shortcuts import render, redirect
from products.models import Purchase, Balance
from orders.forms import OrderCreateForm, AddressCreateForm
from basket.basket import Basket
from profiles.models import Address


def order_create(request):
    if request.user.is_authenticated:
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
                balance = Balance.objects.get(user=request.user.id)
                for item in basket:
                    Purchase.objects.create(order=order,
                                            user=request.user,
                                            product=item['product'],
                                            cost=item['cost'],
                                            quantity=item['quantity'])
                    balance.summ -= item['cost'] * item['quantity']
                    balance.save()
                # очистка корзины
                basket.clear()
                return render(request, 'orders/created.html',
                              {'order': order})
        else:
            form_address = AddressCreateForm
        return render(request, 'orders/create.html',
                      {'basket': basket, "form_address": form_address})

    else:
        return redirect("login")
