# orders/forms.py
from django import forms
from .models import Order


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['flower', 'delivery_address']

