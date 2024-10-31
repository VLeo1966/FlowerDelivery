# catalog/urls.py
from django.urls import path
from .views import flower_list


urlpatterns = [
    path('', flower_list, name='flower_list'),
]

