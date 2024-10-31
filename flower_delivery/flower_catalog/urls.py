# flower_catalog/urls.py
from django.urls import path
from . import views

app_name = 'flower_catalog'

urlpatterns = [
    path('', views.flower_list, name='flower_list'),
    path('<int:pk>/', views.flower_detail, name='flower_detail'),
]

