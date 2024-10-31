# orders/urls.py
from django.urls import path
from . import views

app_name = 'orders'

# Основная страница оформления заказа

urlpatterns = [
    path('create/', views.create_order, name='create_order')
]
