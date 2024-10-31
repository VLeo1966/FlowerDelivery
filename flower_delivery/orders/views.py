from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Order
from .forms import OrderForm

@login_required
def create_order(request, flower_id):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.user = request.user
            order.save()
            return redirect('flower_catalog:flower_list')
    else:
        form = OrderForm(initial={'flower': flower_id})
    return render(request, 'orders/order_form.html', {'form': form})

