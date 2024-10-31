# orders/views.py
from django.shortcuts import render, redirect
from .forms import OrderForm
from flower_delivery.bot.bot import notify_order

def create_order(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.user = request.user
            order.save()
            notify_order(f"New order from {order.user.username}: {order.flower.name} to {order.delivery_address}")
            return redirect('flower_list')
    else:
        form = OrderForm()
    return render(request, 'orders/create_order.html', {'form': form})


