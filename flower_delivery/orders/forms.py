from django import forms
from .models import Order

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['flower', 'quantity', 'delivery_address', 'delivery_date']