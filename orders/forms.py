from django import forms
from .models import Order, Address


class AddressCreateForm(forms.ModelForm):
    class Meta:
        model = Address
        exclude = ['user']


class OrderCreateForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['user', 'address', "status"]


