# flower_delivery/urls.py
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('catalog/', include('catalog.urls')),
    path('orders/', include('orders.urls')),
    path('users/', include('users.urls')),
]


